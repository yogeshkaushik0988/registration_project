# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory data store
registered_users = []

# Valid genders
VALID_GENDERS = ['Male', 'Female', 'Other']

@app.route('/')
def index():
    return "✅ Registration API is running."

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Extract fields
    name = data.get('name')
    surname = data.get('surname')  # Optional
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')
    address = data.get('address')
    submit = data.get('submit')

    # Validate required fields
    if not all([name, email, password, gender, address, submit]):
        return jsonify({"error": "Missing required fields."}), 400

    # Validate gender
    if gender not in VALID_GENDERS:
        return jsonify({"error": "Invalid gender. Choose Male, Female, or Other."}), 400

    # Check if email is already registered
    for user in registered_users:
        if user['email'] == email:
            return jsonify({"error": "Email already registered."}), 409

    # Save user
    user_data = {
        "name": name,
        "surname": surname or "",  # Empty string if not provided
        "email": email,
        "password": password,  # In real apps, hash this!
        "gender": gender,
        "address": address
    }

    registered_users.append(user_data)

    return jsonify({
        "message": "Registration successful.",
        "user": {
            "name": name,
            "surname": surname or "",
            "email": email,
            "gender": gender,
            "address": address
        }
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
