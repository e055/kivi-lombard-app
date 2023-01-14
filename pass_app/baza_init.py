from create_db_auth import create_db_users
from create_db_item import create_db_items, create_db_lombard_items
from create_db_people import create_db, create_db_seeler


def create_DB():
    create_db()
    create_db_seeler()
    create_db_items()
    create_db_lombard_items()
    create_db_users()
