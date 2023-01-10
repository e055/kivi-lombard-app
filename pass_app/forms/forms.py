from flask import render_template, Blueprint

from auth import login_required

forms_bp = Blueprint('forms_endpoints', __name__, template_folder='forms_templates')


@forms_bp.route('/add_form')
@login_required
def add_form():
    return render_template('add.html')


@forms_bp.route('/add_lombard_buy')
@login_required
def add_lombard_buy():
    return render_template('add_lombard_buy.html')


@forms_bp.route('/people_search')
@login_required
def people_search():
    return render_template('people_search.html')


@forms_bp.route('/item_change')
@login_required
def item_change():
    return render_template('item_change.html')


@forms_bp.route('/real_item_change')
@login_required
def real_item_change():
    return render_template('real_item_change.html')


@forms_bp.route('/change_date')
@login_required
def change_date():
    return render_template('change_date.html')


@forms_bp.route('/delete_form')
@login_required
def delete_form():
    return render_template('delete.html')


@forms_bp.route('/index')
@login_required
def index():
    return render_template('index.html')
