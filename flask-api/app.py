from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import routes



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
