# filepath: /c:/Users/extra/Downloads/CareerPilot/backend/src/app.py
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route('/users', methods=['GET'])
    def get_users():
        users = [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Jane Doe'}
        ]
        return jsonify(users)

    @app.route('/search', methods=['GET'])
    def search_user():
        username = request.args.get('username')
        users = [
            {'id': 1, 'name': 'John Doe'},
            {'id': 2, 'name': 'Jane Doe'}
        ]
        user = next((u for u in users if u['name'] == username), None)
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found'}), 404

    @app.route('/add_user', methods=['POST'])
    def add_user():
        data = request.get_json()
        return jsonify({'message': 'User added', 'user': data}), 201

    @app.route('/remove_user', methods=['DELETE'])
    def remove_user():
        data = request.get_json()
        return jsonify({'message': 'User removed', 'user': data}), 200

    return app