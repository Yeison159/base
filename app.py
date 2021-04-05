from flask import Flask, jsonify, request
from controller.Usuario import usuario
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
cors = CORS(app, resources={r"/": {"origins": "*"}})
clase = usuario()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/yeison/', methods=['GET'])
def bienvenida():
    usu = clase.consultarUsuamrio()

    return jsonify(usu)


@app.route('/yeison/<string:name>', methods=['GET', 'POST'])
def parametro(name):
    if request.method == 'POST':
        # data = request.json
        data = request.get_json()
        return jsonify(data['nroCuenta'])
    else:
        return jsonify(name)


@app.route('/user/<int:id>')
def consultar_usuario(id):
    usu = clase.getuser(id)
    if len(usu) == 0:
        return jsonify('no se encontraron registros')
    else:
        return jsonify(usu)


@app.route('/user/')
def consultar_usuario_doce():
    usu = clase.get_doce()
    return jsonify(usu)


if __name__ == '__main__':
    app.run()
