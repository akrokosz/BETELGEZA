from flask import Flask, app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=["GET"])
def home():
    return {"message": "Hello World"}

if __name__ == "__main__":
    app.run(debug=True)
