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
from researcher import client_by_pesel_search, client_by_id_search, researcher

database_bp_searcher = Blueprint('database_endpoints_searcher', __name__)


@database_bp_searcher.route('/add_item', methods=['POST'])
@login_required
def add_item():
    # on_sale = True if request.form.get('on_sale') else False
    client = {}
    value = request.form.get('value')
    val = request.cookies.get('finder')
    # if value == 'pesel':
    #     client = client_by_pesel_search(val)
    #
    # else:
    #     client = client_by_id_search(value)
    #
    # try:
    #     create_item(item_name, take_price, item_sn, redemp_price, date_in, days, owner)
    # except sqlite3.OperationalError:
    #     return "Bad Request", 400

    return redirect('/')


@database_bp_searcher.route('/find_client', methods=['POST'])
@login_required
def find_client():
    client = {}
    value = request.form.get('value')
    val = request.form.get('finder')

    try:
        if value == 'pesel':
            client = client_by_pesel_search(val)

        else:
            client = client_by_id_search(value)

    except sqlite3.OperationalError:
        return "Bad Request", 400
    items = researcher(client['id'])
    context = {
        'client': client['id'],
        'name': client['name'],
        'surname': client['surname'],
        'pesel': client['pesel'],
        'adres': client['adres'],
        'email': client['email'],
        'tel': client['tel'],
        'items': items
    }

    print(client["id"])
    rendered_template = render_template('/people_search.html', **context)
    response = make_response(rendered_template)
    response.set_cookie(key='client_id', value=str(client['id']))

    return response


@database_bp_searcher.route('/delete_item', methods=['POST'])
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
