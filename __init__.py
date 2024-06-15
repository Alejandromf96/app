from flask import Flask
import portfolio

def create_app():
    app = Flask(__name__)

    app.register_blueprint(portfolio.bp)

    return app

app = create_app()

