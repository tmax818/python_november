from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo

#! CREATE
@app.route('/dojo/new')
def new_dojo():
    return render_template('new_dojo.html')

@app.route('/dojo/create', methods=['post'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')
def index():
    return render_template('index.html', dojos = Dojo.get_all())

#! READ ONE

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    data = {'id': id}
    return render_template('show_dojo.html', dojo = Dojo.get_one_with_ninjas(data))



#! UPDATE

@app.route('/dojo/edit/<int:id>')
def edit_dojo(id):
    print(id)
    data = {'id': id}
    return render_template('edit_dojo.html', dojo = Dojo.get_one(data))

@app.route('/dojo/update', methods=['post'])
def update_dojo():
    print(request.form)
    Dojo.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/dojo/delete/<int:id>')
def delete_dojo(id):
    data = {'id': id}
    Dojo.destroy(data)
    return redirect('/')
