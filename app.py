"""Blogly application."""

from flask import Flask, request,render_template, redirect, flash, session
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
#below code won't change any behavior but gets rid of annoying messsage otherwise SQLAlchemy will yell at you
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'hihi'
# will print out SQL version of what you just typed in python
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app )
db.create_all()

@app.route('/')
def homepage():
    return redirect('/users')

@app.route('/users')
def list_users():
    users = User.query.order_by(User.first_name,User.last_name).all()
    return render_template('users/index.html',users=users)

@app.route('/users/new',methods=['GET'])
def new_user_get():
    return render_template('users/new.html')

@app.route('/users/new',methods=['POST'])
def new_user_post():
    new_user = User(first_name=request.form["first_name"], last_name=request.form["last_name"], image_url=request.form["image_url"])

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")
    # return redirect(f'/users/{new_user.id}')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user = user)

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('/users/edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def edited_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"],
    user.last_name = request.form["last_name"],
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
    



# Show the edit page for a user.

# Have a cancel button that returns to the detail page for a user, and a save button that updates the user.




# below code directly run sql on python but uncommon to do this way 
# movies = db.session.execute("SELECT * FROM database")
# list(movies)