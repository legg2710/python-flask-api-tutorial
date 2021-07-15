from flask import Flask
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():

    todos = {"label": "task1", "done": False}

    json_text = flask.jsonify(todos)
    return json_text

    todos = {"label": "task1", "done": False}

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)