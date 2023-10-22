from .import api
from app import db
from flask import request, jsonify
from app.models import User



@api.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
                for user in users]
    return jsonify(user_list)

@api.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    user_data = {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
    return jsonify(user_data)

@api.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'first_name' in data and 'last_name' in data and 'email' in data and 'password' in data:
        new_user = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'],
                        password=data['password'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    else:
        return jsonify({'message': 'Invalid user data'})