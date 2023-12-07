from flask import Flask, request, jsonify

app = Flask(__name__)

class connectdb:
         
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def connectmysql(self):
        import mysql.connector
            
        try:
            mydb = mysql.connector.connect(host = self.host, user = self.user, passwd = self.passwd)
            
            cursur = mydb.cursor()
            cursur.execute("show databases")
            data = cursur.fetchall()

            cursur.close()
            mydb.close()
        
            return mydb, data 
        
        except Exception as e:
            print(e)


    @app.route('/connectdb', methods = ['GET', 'POST'])
    def get_db_details():
        host = request.json('host')
        username = request.json('username')
        password = request.json('password')

        db_connection = connectdb(host, username, password)
        connection, databases  = db_connection.connectmysql()

        dblist = [db[0] for db in databases]


        response = {
        'host': connection._host,
        'user': connection.user,
        'db_list': dblist
    }

        return jsonify(response)
    
if __name__ == '__main__':
    app.run()




