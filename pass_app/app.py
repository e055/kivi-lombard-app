from flask import Flask, render_template, session
from auth import auth_bp
from db_pledge_item import database_bp
from pass_app.forms.forms import forms_bp
from db_buying_items import database_endpoints_buy_item
from db_pledge_changer import database_bp_searcher
from tools import three_days_checker, gold_checker

app = Flask(__name__)

# https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = "123"
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

app.secret_key = SECRET_KEY

app.register_blueprint(auth_bp)
app.register_blueprint(database_bp)
app.register_blueprint(forms_bp)
app.register_blueprint(database_endpoints_buy_item)
app.register_blueprint(database_bp_searcher)


@app.route('/')
def index():
    id_user = session.get('username')
    items = three_days_checker()
    nbp_price, lombard_price = gold_checker()
    context = {
        'id': id_user,
        'username': session.get('id'),
        'items': items,
        'nbp_price': nbp_price,
        'lombard_price': lombard_price
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
