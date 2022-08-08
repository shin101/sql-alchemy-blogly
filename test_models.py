from unittest import TestCase
from app import app
from models import User, db, Post


# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


 
# TEST METHODS MUST START WITH test_ UNDERSCORE!!!
# TO RUN use python -m unittest NAME_OF_FILEs

class BloglyTests(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        User.query.delete()
 
    
    def tearDown(self):
        db.session.rollback()
    
    def test_users(self):
        donkey = User(first_name="donkey", last_name="donks", image_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette1.wikia.nocookie.net%2Fshrek%2Fimages%2F3%2F3d%2FDonkey_From_Shrek.png%2Frevision%2Flatest%2Fscale-to-width-down%2F93%3Fcb%3D20170703204323&f=1&nofb=1')
        self.assertEqual(donkey.last_name,"donks")
    
    def test_fullname(self):
        donkey = User(first_name="donkey", last_name="donks", image_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette1.wikia.nocookie.net%2Fshrek%2Fimages%2F3%2F3d%2FDonkey_From_Shrek.png%2Frevision%2Flatest%2Fscale-to-width-down%2F93%3Fcb%3D20170703204323&f=1&nofb=1')
        self.assertEqual(donkey.full_name, "donkey donks")

    def test_connect_db(self):
        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

class PostTests(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        User.query.delete()
 
    
    def tearDown(self):
        db.session.rollback()

    def test_posts(self):
        post = Post(title="My first blog post", content="this article is going to go viral!")
        self.assertEqual(post.title,"My first blog post")




# def connect_db(app):
#     db.app = app
#     db.init_app(app)
