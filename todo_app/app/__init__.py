from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configure the app (you can add more configurations here)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints (routes, etc.)
    from . import routes
    app.register_blueprint(routes.bp)  # assuming you have a blueprint named 'bp' in routes

    return app
