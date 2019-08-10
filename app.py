#flask and extension
from flask import Flask
#configuration file
from conf import flask_conf

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host=flask_conf.Host, port=flask_conf.Port, debug=flask_conf.Is_debug)