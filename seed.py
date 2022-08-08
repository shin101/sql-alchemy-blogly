from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

# if table isn't empty, empty it
User.query.delete()

# add users
hannah = User(first_name='Hannah', last_name="Montana", image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fonlineordering.rustyspizza.com%2Fimagelibrary%2Fmenu-items%2FPepp.png&f=1&nofb=1")
lizzie = User(first_name='Lizzie', last_name="McGuire", image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fonlineordering.rustyspizza.com%2Fimagelibrary%2Fmenu-items%2FPepp.png&f=1&nofb=1")

post1 = Post(title="my first post", content="nothing to see here", created_at="today")
post2 = Post(title="just for fun", content="this post is not important", created_at="today")


db.session.add_all([hannah,lizzie])

db.session.commit()

db.session.add_all([post1,post2])

db.session.commit()