from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost", user = "root", passwd = "Nishchal@30")
cursor = mydb.cursor()
cursor.execute("create database if not exists APItasks")
cursor.execute("create table if not exists APItasks.tasks(name varchar(50), number int)")


@app.route('/insert', methods = ['POST'])
def insert_data():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("INSERT INTO APItasks.tasks VALUES (%s, %s)", (name, number))
        mydb.commit()
        return jsonify(str('Data inserted successfully'))
    

@app.route('/update', methods = ['POST'])
def update_data():
    if request.method == 'POST':
        updated_name = request.json['updated_name']
        cursor.execute("update APItasks.tasks set number = number + 100 where name = (%s)", (updated_name, ))
        mydb.commit()
        return jsonify(str("Data updated successfully"))


@app.route('/delete', methods = ['POST'])
def delete_data():
    if request.method == 'POST':
        del_data = request.json['delete_name']
        cursor.execute("delete from APItasks.tasks where name = %s", (del_data,))
        mydb.commit()
        return jsonify(str("Record deleted successfully"))
    

@app.route('/fetch', methods = ['POST'])
def fetch_data():
    if request.method == 'POST':
        cursor.execute("select * from APItasks.tasks")
        records = []
        for i in cursor.fetchall():
            records.append(i)
        return jsonify(str(records))


if __name__ =='__main__':
    app.run()

