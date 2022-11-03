from flask_app import app, render_template, request, redirect
from flask_app.models.painting import Painting

#! CREATE
@app.route('/painting/new')
def new_painting():
    return render_template('new_painting.html')

@app.route('/painting/create', methods=['post'])
def create_painting():
    print(request.form)
    Painting.save(request.form)
    return redirect('/')

#! READ ALL
@app.route('/')
def index():
    return render_template('index.html', paintings = Painting.get_all())

#! READ ONE

@app.route('/painting/show/<int:id>')
def show_painting(id):
    data = {'id': id}
    return render_template('show_painting.html', painting = Painting.get_one(data))



#! UPDATE

@app.route('/painting/edit/<int:id>')
def edit_painting(id):
    print(id)
    data = {'id': id}
    return render_template('edit_painting.html', painting = Painting.get_one(data))

@app.route('/painting/update', methods=['post'])
def update_painting():
    print(request.form)
    Painting.update(request.form)
    return redirect('/')

#! DELETE
@app.route('/painting/delete/<int:id>')
def delete_painting(id):
    data = {'id': id}
    Painting.destroy(data)
    return redirect('/')
