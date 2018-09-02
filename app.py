from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

# @app.route('/pokemon/<query>', methods=['GET'])
# def show_content(query):
# 	return 

if __name__ == '__main__':
    app.run()
