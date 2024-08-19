from settings.db import db


class pages(db.Model):
    name = db.Column(db.String(20), unique=True, nullable=False)
    slug = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return self.name
