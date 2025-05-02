from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<b>Hello World from my first Flask app</b>'

@app.route('/json')
def hello_world_json():
    #return {"message": "Hello World from my first Flask app"}
    return jsonify(message="Hello World from my first Flask app")

@app.route('/getOrPost', methods=['GET', 'POST'])
def get_or_post():
    if request.method == 'POST':
        return jsonify(message="This is a POST request",method=request.method),200
    else:
        return jsonify(message="This is a GET request",method=request.method),200