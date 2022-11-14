from flask import Flask, render_template
import requests
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://rickandmortyapi.com/api/character"
    data = requests.get(url).json()
    pprint(data)
    return render_template('index.html', data = data)

@app.route('/<episode>')
def show_episode(episode):
    url = f"https://rickandmortyapi.com/api/{episode}"
    data = requests.get(url).json()
    pprint(data)
    return render_template('episode.html', data = data)
    

if __name__ == '__main__':
    app.run(debug=True)