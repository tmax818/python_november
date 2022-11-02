from flask_app import app, render_template, request, redirect
from flask_app.models.user import User

#! READ ALL
@app.route('/')
def index():
    return render_template('index.html', users = User.get_all())

#! READ ONE


#! CREATE
@app.route('/user/new')
def new_user():
    return render_template('new_user.html')

@app.route('/user/create', methods=['post'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

#! UPDATE

@app.route('/user/edit/<int:id>')
def edit_user(id):
    print(id)
    return "future home of edit page"

@app.route('/user/update')
def update_user():
    pass


#! DELETE
