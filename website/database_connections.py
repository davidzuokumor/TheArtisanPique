import mysql.connector
from sqlalchemy.testing.config import db_opts


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="Project1234",
        database="artisandb"
    )
    return connection

#cursor.execute("SELECT * FROM table")
#result = cursor.fetchall()



