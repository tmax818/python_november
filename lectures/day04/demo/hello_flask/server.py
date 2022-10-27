from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    number = 1
    return render_template('index.html', number = number, is_cool = False)

@app.route('/<int:number>')          # The "@" decorator associates this route with the function immediately following
def hello_world(number):
    return render_template('index.html', number = number)  # Return the string 'Hello World!' as a response

@app.route('/<color>')
def change_color(color):
    number = 1
    return render_template('index.html', color = color, number = number)

@app.route('/about')
def about():
    return render_template('about.html')

print(__name__)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

