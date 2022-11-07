from flask_app import app, render_template, redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/new_dojo', methods=['post'])
def dojos_create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojos_show(id):
    data = {'id': id}
    return render_template('show_dojo.html', dojo = Dojo.get_one(data))