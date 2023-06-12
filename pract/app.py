from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo FLASK"

if __name__ == "__main__":
    app.run(port=5000)