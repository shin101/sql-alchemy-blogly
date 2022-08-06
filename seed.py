from models import User, db
from app import app

db.drop_all()
db.create_all()

# if table isn't empty, empty it
User.query.delete()

# add users
hannah = User(first_name='Hannah', last_name="Montana", image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fonlineordering.rustyspizza.com%2Fimagelibrary%2Fmenu-items%2FPepp.png&f=1&nofb=1")

lizzie = User(first_name='Lizzie', last_name="McGuire", image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fonlineordering.rustyspizza.com%2Fimagelibrary%2Fmenu-items%2FPepp.png&f=1&nofb=1")


db.session.add(hannah)
db.session.add(lizzie)

db.session.commit()