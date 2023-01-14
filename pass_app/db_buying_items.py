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
from pass_app.researcher import researcher_by_id_lombard_items
from changer import lombard_item_changer

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
    try:
        person = id_seeler_search(pesel)
    except sqlite3.OperationalError:
        return "Bad Request", 400

    context = {
        'seeler': person
    }
    p2 = str(person)
    rendered_template = render_template('/add_lombard_buy.html', **context)
    response = make_response(rendered_template)
    response.set_cookie(key='new_seller_id', value=p2)

    return response


@database_endpoints_buy_item.route('/find_sell_item', methods=['POST'])
@login_required
def find_sell_item():
    id_item_cookie = request.cookies.get('id_item')
    id_item = request.form.get('id_item')
    value_item = request.form.get('value_item')
    try:
        item = item_finder(id_item, id_item_cookie)
        if len(item) == 0:
            context = {'error': 'Błędnie wprowadzone ID przedmiotu, spróbuj jeszcze raz'}
            return render_template('/find_sell_item.html', **context)
        item_id = item_id_checker(id_item, id_item_cookie)
    except:
        render_templat = render_template('/')
        response = make_response(render_templat)
        return response
    name = item[0][1]
    s_n = item[0][2]
    value = item[0][3]
    prop_value = item[0][4]
    sold = item[0][6]
    try:
        if int(sold) == 0:
            sold = 0
    except:
        sold = item[0][6]

    if value_item:
        try:
            lombard_item_changer(int(item_id), int(value_item))
        except sqlite3.OperationalError:
            return "Bad Request", 400
        rendered_template = render_template('/accepted_operation.html')
        response = make_response(rendered_template)

        return response

    else:
        context = {
            'id_item': id_item,
            'name': name,
            's_n': s_n,
            'value': value,
            'prop_value': prop_value,
            'sold': sold
        }

        rendered_template = render_template('/find_sell_item.html', **context)
        response = make_response(rendered_template)
        response.set_cookie(key='id_item', value=id_item)
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


def item_finder(item_id, item_id_cookie):
    if item_id:
        item = researcher_by_id_lombard_items(item_id)
    else:
        item = researcher_by_id_lombard_items(item_id_cookie)
    return item


def item_id_checker(item_id, item_id_cookie):
    if item_id:
        item = item_id
    else:
        item = item_id_cookie
    return item
