import sqlite3
from flask import Blueprint, request, render_template, make_response
from auth import login_required
from db_utils import get_connection
from datetime import date
from baza_add_person import create_seeler
from id_by_pesel_search import id_seeler_search
from werkzeug.utils import redirect
from baza_add_item import create_lombard_item
from calc_settings import lombard_items_val

database_endpoints_buy_item = Blueprint('database_endpoints_buy', __name__)


@database_endpoints_buy_item.route('/add_lombard_item', methods=['POST'])
@login_required
def add_lombard_item():
    # on_sale = True if request.form.get('on_sale') else False
    item_name = request.form.get('item_name')
    take_price = request.form.get('price')
    item_sn = request.form.get('item_sn')
    date_in = date.today()
    date_in = str(date_in)
    owner = request.cookies.get('new_seller_id')
    sugest_price = lombard_items_val(take_price)
    try:
        create_lombard_item(item_name, take_price, item_sn, sugest_price, date_in, owner)
    except sqlite3.OperationalError:
        return "Bad Request", 400

    return redirect('/')


@database_endpoints_buy_item.route('/add_seeler', methods=['POST'])
@login_required
def add_seeler():
    name = request.form.get('name')
    surname = request.form.get('surname')
    pesel = request.form.get('pesel')
    email = request.form.get('email')
    phone = request.form.get('phone')
    try:
        create_seeler(name, surname, pesel, email, phone)
    except sqlite3.OperationalError:
        return "Bad Request", 400
    person = id_seeler_search(pesel)
    context = {
        'seeler': person
    }
    p2 = str(person)
    rendered_template = render_template('/add_lombard_buy.html', **context)
    response = make_response(rendered_template)
    response.set_cookie(key='new_seller_id', value=p2)

    return response


@database_endpoints_buy_item.route('/delete_item', methods=['POST'])
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
