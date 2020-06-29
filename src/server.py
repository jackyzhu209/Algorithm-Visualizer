from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def homepage():
    return send_from_directory('static', 'algos.html')


@app.route('/<path:filename>')
def staticfile(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    Flask.run(app, port=8080, debug=True)