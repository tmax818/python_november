from flask_app import app, render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninja(): 
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/ninja_new', methods = ['post'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")