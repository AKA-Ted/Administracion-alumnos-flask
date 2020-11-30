from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return "<h1>Administración de Alumnos</h1>"

if __name__ == "__main__":
    app.run(debug = True)