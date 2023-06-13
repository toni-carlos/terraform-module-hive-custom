from flask import Flask

from src.routes import execute_sql_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(execute_sql_blueprint, url_prefix="/create-alter-table")
    return app


if __name__ == "__main__":
    create_app().run(debug=True)