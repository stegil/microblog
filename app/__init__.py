from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config


app = Flask(__name__)

# Configuration
app.config.from_object(Config)

# flask-sqlalchemy & flask-migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# flask-login
login = LoginManager(app)
login.login_view = "login"  # redirect if not logged in


from app import routes, models
