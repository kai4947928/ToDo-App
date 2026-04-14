from flask import Flask, render_template
from config import Config
from app.db import init_db, close_db
from app.routes.auth import auth_bp
from app.routes.tasks import tasks_bp

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    return app