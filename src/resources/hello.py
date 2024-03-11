from flask import Blueprint, jsonify

hello = Blueprint('hello', __name__)

@hello.route('/hello', methods=['GET'])
def get_hello():
    return jsonify({'message': 'Hello World!'})