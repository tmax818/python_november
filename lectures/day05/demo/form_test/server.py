from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "any string you want"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def handle_data():
    print(request.form)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)