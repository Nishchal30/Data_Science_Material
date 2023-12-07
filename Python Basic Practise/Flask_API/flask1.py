from flask import Flask, request, jsonify

app = Flask(__name__) # Object of the class Flask

# @ is annotation, just after this line call whatever writtem immediate next to this line.
# 'abc/' is the route where we want to route our function

# There are two types of sending data to accept the response
# 1) Pass in URL so that anyone can see that data (Not safe)
# 2) Pass in the Body so that no one can see that data (safest)

# GET :- passing a data in URL

# POST :- passing a data in the body

@app.route('/abc', methods = ['GET', 'POST']) # Its a decorator from this route our function will be called
def test1(a, b):
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        
        return jsonify((result))
    

@app.route('/abc1', methods = ['GET', 'POST']) 
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        
        return jsonify((result))
    
@app.route('/abc2', methods = ['GET', 'POST']) 
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        
        return jsonify((result))
    
@app.route('/abc3', methods = ['GET', 'POST']) 
def test4():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        
        return jsonify((result))
    
@app.route('/test')
def testfun():
    get_name = request.args.get("get_name")
    return "The test function with {}".format(get_name)

if __name__ == '__main__':
    app.run(port=5004, debug=True)

    # Whenever we write debug = True, it always restarts the app autmatically after saving our changes. 
    # We don't need to restart the app manually all the time

