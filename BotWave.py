from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(debug=False, port=port, host='127.0.0.1')
