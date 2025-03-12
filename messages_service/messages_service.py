from flask import Flask

app = Flask(__name__)

@app.route("/get_message", methods=["GET"])
def get_message():
    return "not implemented yet", 200

if __name__ == "__main__":
    app.run(port=8081)