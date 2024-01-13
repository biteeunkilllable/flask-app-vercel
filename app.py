from flask import Flask
from modules import modules

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
