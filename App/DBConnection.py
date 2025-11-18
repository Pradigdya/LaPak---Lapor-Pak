import sqlite3

from werkzeug.security import generate_password_hash

DB_NAME = "UTS8.db"

def get_db_connection():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn