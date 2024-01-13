from flask import Flask
from modules import modules

app = Flask(__name__)

@app.route("/")
def index():
    content = modules.content()
    return content


if __name__ == "__main__":
    app.run(debug=True)
