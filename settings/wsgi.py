from flask import Flask
from home import Home

app = Flask(__name__)
app.config.from_pyfile("settings", silent=True)

app.register_blueprint(Home)
