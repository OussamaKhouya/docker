from flask import Blueprint, request, jsonify, abort
from .models import User, db
from . import cache

bp = Blueprint('api', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or not data.get('username') or not data.get('email'):
        abort(400, "Missing username or email")
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    cached = cache.get(f'user:{id}')
    if cached:
        return cached, 200
    user = User.query.get_or_404(id)
    response = jsonify(user.to_dict())
    cache.set(f'user:{id}', response.get_data(), ex=60)  # cache 60 seconds
    return response

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    if not data:
        abort(400)
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    cache.delete(f'user:{id}')  # invalidate cache
    return jsonify(user.to_dict())

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    cache.delete(f'user:{id}')
    return '', 204
