from app import create_app
from os import environ

from flask import Flask, jsonify


from controllers import StatisticsController


app = Flask(__name__)
import preloaded
preloaded.init()

app.register_blueprint(StatisticsController)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
