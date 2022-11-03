from flask_app import app, render_template, request, redirect
from flask_app.models.user import User

#! CREATE
@app.route('/user/new')
def new_user():
    return render_template('new_user.html')

@app.route('/user/create', methods=['post'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')
def index():
    return render_template('index.html', users = User.get_all())

#! READ ONE

@app.route('/user/show/<int:id>')
def show_user(id):
    data = {'id': id}
    return render_template('show_user.html', user = User.get_one_with_pets(data))



#! UPDATE

@app.route('/user/edit/<int:id>')
def edit_user(id):
    print(id)
    data = {'id': id}
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/user/update', methods=['post'])
def update_user():
    print(request.form)
    User.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {'id': id}
    User.destroy(data)
    return redirect('/')
