from os import environ

from flask import Flask, jsonify


from controllers import StatisticsController


def create_app():
    app = Flask(__name__)
    import preloaded
    preloaded.init()

    app.register_blueprint(StatisticsController)

    return app
