from flask import Flask, request, jsonify
from pprint import pprint as pp

app = Flask(__name__)

@app.route("/verify", methods=['GET', 'POST'])
def callback():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
