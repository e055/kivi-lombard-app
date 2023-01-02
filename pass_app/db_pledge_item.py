import sqlite3
from flask import Blueprint, request, render_template, make_response
from auth import login_required
from db_utils import get_connection
from datetime import date
from baza_add_person import create_person
from id_by_pesel_search import id_search
from werkzeug.utils import redirect
from baza_add_item import create_item
from calc_settings import items_val

database_bp = Blueprint('database_endpoints', __name__)


@database_bp.route('/add_item', methods=['POST'])
@login_required
def add_item():
    # on_sale = True if request.form.get('on_sale') else False
    item_name = request.form.get('item_name')
    take_price = request.form.get('price')
    item_sn = request.form.get('item_sn')
    date_in = date.today()
    date_in = str(date_in)
    days = request.form.get('days')
    owner = request.cookies.get('newid')

    print(item_name)
    print(item_sn)
    print(date_in)
    print(days)
    print(owner)
    redemp_price = items_val(take_price, days)
    print(redemp_price)
    try:
        create_item(item_name, take_price, item_sn, redemp_price, date_in, days, owner)
    except sqlite3.OperationalError:
        return "Bad Request", 400

    return redirect('/')


@database_bp.route('/add_person', methods=['POST'])
@login_required
def add_person():
    name = request.form.get('name')
    surname = request.form.get('surname')
    pesel = request.form.get('pesel')
    adres = request.form.get('adress')
    email = request.form.get('email')
    phone = request.form.get('phone')

    try:
        create_person(name, surname, pesel, adres, email, phone)
    except sqlite3.OperationalError:
        return "Bad Request", 400
    print(pesel)
    person = id_search(pesel)
    print(person)
    context = {
        'person': person
    }
    p2 = str(person)
    rendered_template = render_template('/add.html', **context)
    response = make_response(rendered_template)
    response.set_cookie(key='newid', value=p2)

    return response


@database_bp.route('/delete_item', methods=['POST'])
@login_required
def delete_item():
    item_id = request.form['id']

    conn = get_connection()
    c = conn.cursor()

    query = 'DELETE FROM "items" WHERE "id" = ?'
    params = (item_id,)

    c.execute(query, params)
    conn.commit()

    return redirect('/')
