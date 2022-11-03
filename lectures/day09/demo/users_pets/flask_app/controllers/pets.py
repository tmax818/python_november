from flask_app import app, render_template, request, redirect
from flask_app.models.pet import Pet
from flask_app.models.user import User

#! CREATE
@app.route('/pet/new')
def new_pet():
    return render_template('new_pet.html', users=User.get_all())

@app.route('/pet/create', methods=['post'])
def create_pet():
    print(request.form)
    Pet.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/pets')
def pets():
    return render_template('pets.html', pets = Pet.get_all())

#! READ ONE
@app.route('/pet/show/<int:id>')
def show_pet(id):
    data = {'id': id}
    return render_template('show_pet.html', pet = Pet.get_one(data))

#! UPDATE
@app.route('/pet/edit/<int:id>')
def edit_pet(id):
    print(id)
    data = {'id': id}
    return render_template('edit_pet.html', pet = Pet.get_one(data))

@app.route('/pet/update', methods=['post'])
def update_pet():
    print(request.form)
    Pet.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/pet/delete/<int:id>')
def delete_pet(id):
    data = {'id': id}
    Pet.destroy(data)
    return redirect('/')
