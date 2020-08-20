from flask import Flask, send_from_directory, request
import Algorithms

app = Flask(__name__)


@app.route('/')
def homepage():
    return send_from_directory('static', 'algos.html')


@app.route('/<path:filename>')
def static_file(filename):
    return send_from_directory('static', filename)


@app.route('/images/<path:image>')
def images(image):
    return send_from_directory('images', image)


@app.route('/updateGraph', methods=['POST'])
def update():
    data = request.data
    print(data)
    return Algorithms.updateGraph(data)


@app.route('/newGraph', methods=['POST'])
def newGraph():
    return Algorithms.newGraph()


@app.route('/runAlgo', methods=['POST'])
def runAlgo():
    data = request.data
    print(data)
    return Algorithms.runAlgorithm(data)

if __name__ == "__main__":
    Flask.run(app, debug=True)