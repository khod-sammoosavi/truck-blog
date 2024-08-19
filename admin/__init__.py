import os
from main import BASE_DIR
from flask import Blueprint

template_dir = os.path.join(BASE_DIR, "admin/templates")
static_dir = os.path.join(BASE_DIR, "admin/static")

Admin = Blueprint("Admin", __name__, url_prefix="/admin", template_folder=template_dir, static_folder=static_dir)

from admin.views import views
views()
