```python
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from flask_mongoengine import MongoEngine
from mongoengine import DoesNotExist

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = MongoEngine(app)

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    new_user.save()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = User.objects.get(username=data['username'])
        if bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=data['username'])
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except DoesNotExist:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```