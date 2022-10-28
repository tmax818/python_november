from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')
def index():
    users = [
   {'id': 1, 'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'id': 2, 'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'id': 3, 'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'id': 4, 'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template('index.html', users = users)



print(__name__)
if __name__=="__main__":   
    app.run(debug=True)    

