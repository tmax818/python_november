from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "any string you want..."


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1

    return render_template('index.html')

@app.route('/up')
def up():
    session['count'] += 2
    return redirect('/')


@app.route('/handle_form', methods = ['POST'])
def handle_form():
    print(request.form)
    session['key'] = request.form['key']
    return redirect('/')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)