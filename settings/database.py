from settings.wsgi import app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
Migrate(app, db)


from admin import models
