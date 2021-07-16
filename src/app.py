import flask
import json
from flask import Flask
app = Flask(__name__)

todos = [
    { "label": "Task1", "done": False },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    global todos
    json_text = flask.jsonify(todos)
    return json_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)