from flask_app import app, render_template, redirect, request, bcrypt, session
from flask_app.models.user import User

@app.route('/')
def index():
    password = bcrypt.generate_password_hash('password')
    password_valid = bcrypt.check_password_hash(password, 'password')
    print(password, password_valid)
    return render_template('index.html')

#! CREATE AKA REGISTER

@app.route("/register", methods = ['post'])
def register():
    print(request.form)

    # TODO validate our user
    if not User.validate_user(request.form):
        return redirect('/')
    # TODO hash the password
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    # TODO save the user to the database
    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user_id = User.save(user_data)
    # TODO log in the user
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    
    return redirect('/things')

@app.route('/things')
def things():
    return f"<h1> Welcome {session['first_name']} to our app!!"



#! READ and VERIFY AKA LOGIN


#! LOGOUT

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

