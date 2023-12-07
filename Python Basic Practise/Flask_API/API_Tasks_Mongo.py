from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Nishchal30:Nishchal30@cluster0.9omin78.mongodb.net/")
database = client['API_Tasks']
collection = database['Tasks']


@app.route('/insert/mongo', methods = ['POST'])
def insert_mongo():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("The data inserted successfully"))

    
if __name__ == "__main__":
    app.run()