from flask import Flask
import os
import portfolio

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    app.register_blueprint(portfolio.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)