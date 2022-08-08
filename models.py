"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


# models go below 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    first_name = db.Column(db.Text,nullable=False)
    last_name = db.Column(db.Text,nullable=False)
    image_url = db.Column(db.Text,nullable=False)

    posts = db.relationship('Post',backref='user')

    @property
    def full_name(self) :
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        x = self
        return f"<User id={x.id} first_name={x.first_name} last_name={x.last_name} url={x.url}>"




class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

def get_user_info():
    all_fnames = User.query.all()
    for name in all_fnames:
        # if name.posts is not None:
        #     print(name.first_name, name.title)
        # else:
        print(name.first_name, name.last_name, name.image_url)


    # on iPython db.create_all()


    def __repr__(self):
        x = self
        return f"<Post id={x.id} post_title={x.title} post_content={x.content}>"

def connect_db(app):
    db.app = app
    db.init_app(app)