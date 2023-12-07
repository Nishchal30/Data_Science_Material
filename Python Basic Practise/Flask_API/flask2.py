from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

@app.route('/ ')
def get_details_db():
    mydb = conn.connect(host = "localhost", user = "root", passwd = "Nishchal@30")
    cursor = mydb.cursor()
    database = request.args.get("database_name")
    table = request.args.get("table_name")
    cursor.execute("Select * from {}.{}".format(database, table))
    result = cursor.fetchall()
    return result

if __name__ == "__main__":
    app.run()