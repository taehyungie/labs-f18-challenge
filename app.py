from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<string:query>', methods=['GET'])
def show_content(query):
	r = requests.get('http://pokeapi.co/api/v2/pokemon-form/'+ query)
	pokemonName = print(r.json()['name'])
	pokemonId = print(r.json()['id'])
	return render_template('test.html', pokemonName=r.json()['name'], pokemonId=r.json()['id'])

if __name__ == '__show_content__':
    app.run() 

if __name__ == '__main__':
    app.run()


