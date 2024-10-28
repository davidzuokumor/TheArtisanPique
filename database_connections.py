import mysql.connector


db = mysql.connector.connect(
    host="your_database_host",
    user="user",
    password="your_password",
    database="artisandb"
)

cursor = db.cursor()

# Example query
#cursor.execute("SELECT * FROM your_table_name")
#result = cursor.fetchall()
#print(result)

db.close()
