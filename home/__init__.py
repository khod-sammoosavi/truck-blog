from flask import Blueprint

Home = Blueprint("Home", __name__, url_prefix="/")

from .views import views

views()
