from flask_app import app, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#! CREATE
@app.route('/ninja/new')
def new_ninja():
    return render_template('new_ninja.html', users=User.get_all())

@app.route('/ninja/create', methods=['post'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', ninjas = Ninja.get_all())

#! READ ONE
@app.route('/ninja/show/<int:id>')
def show_ninja(id):
    data = {'id': id}
    return render_template('show_ninja.html', ninja = Ninja.get_one(data))

#! UPDATE
@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    print(id)
    data = {'id': id}
    return render_template('edit_ninja.html', ninja = Ninja.get_one(data))

@app.route('/ninja/update', methods=['post'])
def update_ninja():
    print(request.form)
    Ninja.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    data = {'id': id}
    Ninja.destroy(data)
    return redirect('/')
