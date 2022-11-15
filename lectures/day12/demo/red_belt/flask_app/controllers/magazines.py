from flask_app import app, render_template, request, redirect, session
from flask_app.models.magazine import Magazine


#! CREATE
@app.route('/magazine/new')
def new_magazine():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new_magazine.html')

@app.route("/magazine/create", methods = ['post'])
def create_magazine():
    print(request.form)
    if not Magazine.validate_magazine(request.form):
        return redirect('/magazine/new')
    Magazine.save(request.form)
    return redirect('/magazines')

#! READ ALL
@app.route('/magazines')
def magazines():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('magazines.html', magazines = Magazine.get_all())

#! READ ONE

@app.route('/magazines/<int:id>')
def show_magazine(id):
    data = {'id': id}
    return render_template('show_magazine.html', magazine = Magazine.get_one(data))

#! UPDATE

@app.route('/magazines/edit/<int:id>')
def edit_magazine(id):
    data = {'id': id}
    return render_template('edit_magazine.html', magazine = Magazine.get_one(data))

@app.route("/magazines/update", methods = ['post'])
def update_magazine():
    print(request.form)
    if not Magazine.validate_magazine(request.form):
        return redirect(f"/magazines/edit/{request.form['id']}")
    Magazine.update(request.form)
    return redirect('/magazines')

#! DELETE

@app.route('/magazines/destroy/<int:id>')
def destroy_magazine(id):
    data = {'id': id}
    Magazine.destroy(data)
    return redirect('/magazines')