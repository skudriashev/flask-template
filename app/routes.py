from flask import request

from .app import app
from .models import db, User


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        return {
            'users': [
                {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                }
                for user in users
            ]
        }
    elif request.method == 'POST':
        data = request.json
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
