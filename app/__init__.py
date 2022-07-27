from flask import Flask
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)

# import blueprints
from .auth.routes import auth


# register blueprints
app.register_blueprint(auth)

app.config.from_object(Config)

from . import routes
# from . import models