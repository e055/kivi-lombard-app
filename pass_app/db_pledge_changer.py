import sqlite3
from flask import Blueprint, request, render_template, make_response
from auth import login_required
from db_utils import get_connection
from werkzeug.utils import redirect
from calc_and_date import date_count
from researcher import client_by_pesel_search, client_by_id_search, researcher, researcher_by_id
from changer import item_changer, date_item_changer

database_bp_searcher = Blueprint('database_endpoints_searcher', __name__)


@database_bp_searcher.route('/item_change', methods=['POST'])
@login_required
def item_change():
    item_id_c = request.form.get('item_id_c')
    item = researcher_by_id(item_id_c)
    try:
        if len(item) == 0:
            context = {'error': 'Błędnie wprowadzone ID przedmiotu, spróbuj jeszcze raz'}
            return render_template('/people_search.html', **context)
    except sqlite3.OperationalError:
        return "Bad Request", 400

    name = item[0][1]
    s_n = item[0][2]
    value = item[0][4]
    context = {
        'name': name,
        'serial_n': s_n,
        'value': value
    }

    rendered_template = render_template('/item_change.html', **context)
    response = make_response(rendered_template)
    response.set_cookie(key='item_id', value=item_id_c)

    return response


@database_bp_searcher.route('/real_item_change', methods=['POST'])
@login_required
def real_item_change():
    item_value = request.form.get('item_value')
    item_id = request.cookies.get('item_id')
    item = researcher_by_id(item_id)
    value = item[0][4]

    calc = value - float(item_value)

    try:
        item_changer(calc, item_id)
    except sqlite3.OperationalError:
        return "Bad Request", 400

    context = {
        'item_value': item_value,
        'value': calc
    }

    rendered_template = render_template('/real_item_change.html', **context)
    response = make_response(rendered_template)

    return response


@database_bp_searcher.route('/change_date', methods=['POST'])
@login_required
def change_date():
    days = request.form.get('days')
    item_id = request.cookies.get('item_id')
    item = researcher_by_id(item_id)

    name = item[0][1]
    date_out = item[0][6]
    new_date = date_count(date_out, days)
    try:
        date_item_changer(new_date, item_id)
    except sqlite3.OperationalError:
        return "Bad Request", 400
    context = {
        'name': name,
        'date_out': date_out
    }

    rendered_template = render_template('/change_date.html', **context)
    response = make_response(rendered_template)

    return response


@database_bp_searcher.route('/find_client', methods=['POST'])
@login_required
def find_client():
    client = {}
    value = request.form.get('value')
    val = request.form.get('finder')

    try:
        if value == 'pesel':
            client = client_by_pesel_search(val)
            if client == 0:
                context = {'error': 'Błędnie wprowadzone dane, spróbuj jeszcze raz'}
                return render_template('/people_search.html', **context)

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
