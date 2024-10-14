from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import jwt_required, \
    JWTManager, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
      "user1": {
          "username": "user1",
          "password": generate_password_hash("bonjour"),
          "role": "user"
          },
      "admin1": {
          "username": "admin1",
          "password": generate_password_hash("hello"),
          "role": "admin"
          }
  }

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

app.config['JWT_SECRET_KEY'] = 'AyGel32@'
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401

@app.route("/admin-only")
@jwt_required()
def admin_only():
    
    current_user = get_jwt_identity()
    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401



if __name__ == '__main__':
    app.run(debug=True)
