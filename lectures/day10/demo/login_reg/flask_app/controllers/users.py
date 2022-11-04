from flask_app import app, render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

#! CREATE AKA REGISTER

@app.route("/register", methods = ['post'])
def register():
    print(request.form)
    # TODO validate our user
    if not User.validate_user(request.form):
        return redirect('/')
    # TODO hash the password
    # TODO save the user to the database
    # TODO log in the user
    return redirect('/things')



#! READ and VERIFY AKA LOGIN


#! LOGOUT

