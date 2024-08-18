import os
from main import BASE_DIR
from flask import Blueprint


template_dir = os.path.join(BASE_DIR, "home/templates")
static_dir = os.path.join(BASE_DIR, "home/static")

Home = Blueprint("Home", __name__, url_prefix="/", template_folder=template_dir, static_folder=static_dir)

from .views import views

views()
