from main import BASE_DIR


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/db.sqlite3"

class Development(Config):
    HOST = "0.0.0.0"
    PORT = "5000"
    DEBUG = True

class Production(Config):
    DEBUG = False
