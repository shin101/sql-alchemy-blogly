"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# models go below 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    first_name = db.Column(db.Text,nullable=False)
    last_name = db.Column(db.Text,nullable=False)
    image_url = db.Column(db.Text,nullable=False)

    @property
    def full_name(self) :
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    db.app = app
    db.init_app(app)

def __repr__(self):
    x = self
    return f"<User id={x.id} first_name={x.first_name} last_name={x.last_name} url={x.url}>"