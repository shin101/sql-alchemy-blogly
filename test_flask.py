from unittest import TestCase
from app import app
from models import User, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UsersTestCase(TestCase):
    def setUp(self):
        User.query.delete()

        user = User(first_name="cotton", last_name="candy", image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fplay-lh.googleusercontent.com%2FiHicjCOT-R-SiK-OeE3xt4ZmzSThYiwF1SspifKxDBFLEPweCA78ADCivt-lgmfZgdw%3Ds180&f=1&nofb=1")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    """test to see if root is working"""
    def test_root(self):
        with app.test_client() as client:
            res = client.get("/")
            self.assertEqual(res.status_code, 302)


    """check to see if user correctly added to show.html page"""
    def test_new_user(self):
        with app.test_client() as client:
            res = client.get('/users/3')
            html = res.get_data(as_text=True)
            self.assertIn('<h2>cotton candy</h2>',html)


    # # """test to see if edit page renders correctly. must run below code separately to make it work"""
    def test_edit_page(self):
        with app.test_client() as client:
            d = {"first_name":"cotton", "last_name":"chocolate", "image_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fplay-lh.googleusercontent.com%2FiHicjCOT-R-SiK-OeE3xt4ZmzSThYiwF1SspifKxDBFLEPweCA78ADCivt-lgmfZgdw%3Ds180&f=1&nofb=1"}
            res = client.post('/users/2/edit', data=d, follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<li><a href="/users/2">cotton chocolate</a></li>', html)
           


    """test if cotton candy sucessfully deleted"""
    def test_delete(self):
            with app.test_client() as client:
                res = client.get('/users/1/delete',follow_redirects=True)
                html = res.get_data(as_text=True)
                self.assertEqual(res.status_code, 200)
                self.assertIn('<h2>Users</h2>', html)
                self.assertIn('<ul>\n    \n  </ul>', html)


