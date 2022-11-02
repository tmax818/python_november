from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
from thing import Thing
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "any string you want"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # things_from_db is the list of thing objects from the class method: get_all
    things_from_db = Thing.get_all()
    return render_template('index.html', things = things_from_db)  # Return the string 'Hello World!' as a response

@app.route('/handle_form', methods=['POST'])
def handle_form():
    print(request.form)
    session['title'] = request.form['title']
    Thing.save(request.form)
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

