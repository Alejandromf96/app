from flask import Flask
import portfolio

def create_app():
    app = Flask(__name__)

    app.register_blueprint(portfolio.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
