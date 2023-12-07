from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

class connectdb:
         
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.mydb = None
        self.cursor = None

    def connect_db(self):

        try:
            self.mydb = mysql.connector.connect(host = self.host, user = self.user, passwd = self.passwd)
            self.cursor = self.mydb.cursor()
            self.cursor.execute("use ineuron")

            return True

        except Exception as e:
            print(e)
            return False

    def insert_data(self, values):
        try:
            # cursur.execute("use ineuron")
            sql = "INSERT INTO bank_details (age, job, marital,education, `default`, balance, housing, loan, contact, `day`, `month`, duration, campaign, pdays, previous, poutcome, y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            self.cursor.execute(sql, values)
                        
            self.mydb.commit()

            self.cursor.close()
            self.mydb.close()

            return "Data inserted successfully"
        
        except Exception as e:
            print(e)

            return "Data insertion failed"


    @app.route('/insertdb', methods = ['GET', 'POST'])
    def get_db_details():
        host = request.json('host')
        username = request.json('username')
        password = request.json('password')

        db_connection = connectdb(host, username, password)
        db_connection.connect_db()
        result = db_connection.insert_data(values=[42, 'entrepreneur', 'divorced', 'tertiary', 'yes', 2, 'yes', 'no', 'unknown', 5, 'may', 380, 1, -1, 0, 'unknown', 'no'])

        return jsonify({"message" : result})
    
if __name__ == '__main__':
    app.run()



# from flask import Flask, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# class ConnectDB:
#     def __init__(self, host, user, passwd):
#         self.host = host
#         self.user = user
#         self.passwd = passwd
#         self.mydb = None
#         self.cursor = None

#     def connect_mysql(self):
#         try:
#             self.mydb = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd)
#             self.cursor = self.mydb.cursor()
#             self.cursor.execute("use ineuron")
#             return True
#         except Exception as e:
#             print(e)
#             return False

#     def insert_data(self, values):
#         try:
#             sql = "INSERT INTO bank_details (age, job, marital, education, `default`, balance, housing, loan, contact, `day`, `month`, duration, campaign, pdays, previous, poutcome, y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#             self.cursor.executemany(sql, values)
#             self.mydb.commit()
#             return "Data inserted successfully"
#         except Exception as e:
#             print(e)
#             return "Data insertion failed"

# @app.route('/insert-data', methods=['POST'])
# def insert_data_to_db():
#     try:
#         data = request.get_json()
#         values = data.get('values')

#         if not values:
#             return jsonify({"message": "Values not provided in the request body"}), 400

#         db_connection = ConnectDB("localhost", "your_username", "your_password")
#         if db_connection.connect_mysql():
#             result = db_connection.insert_data(values)
#             return jsonify({"message": result}), 200
#         else:
#             return jsonify({"message": "Database connection failed"}), 500

#     except Exception as e:
#         return jsonify({"message": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)





