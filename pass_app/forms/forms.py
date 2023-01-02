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


@forms_bp.route('/delete_form')
@login_required
def delete_form():
    return render_template('delete.html')
