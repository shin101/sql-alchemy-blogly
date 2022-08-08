"""Blogly application."""

from flask import Flask, request,render_template, redirect, flash
from models import db, connect_db, User, Post, get_user_info
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
def show_user(user_id,):
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
    
@app.route('/users/<int:user_id>/posts/new')
def post_user(user_id):
    """what happens when you click add post"""
    user = User.query.get_or_404(user_id)
    return render_template("posts/new.html", user=user)

@app.route('/users/<int:user_id>/posts/new',methods=['POST'])
def add_post(user_id):
    """what happens after you submit post"""
    user = User.query.get_or_404(user_id)

    new_post = Post(title = request.form['title'],content = request.form['content'],user=user)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    """what happens when you click add post"""
    post = Post.query.get_or_404(post_id)
    return render_template("posts/show.html", post=post)


@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('/posts/edit.html', post=post)



@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edited_post(post_id):
    """takes care of the part where you edit a post"""
    post = Post.query.get_or_404(post_id)
    post.title = request.form["title"],
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")


@app.route('/posts/<int:post_id>/delete',methods=['POST'])
def delete_post(post_id):
    '''deleting a post'''
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')
# below code directly run sql on python but uncommon to do this way 
# movies = db.session.execute("SELECT * FROM database")
# list(movies)