from flask import Flask

app = Flask(__name__)

# defines path/route
@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)