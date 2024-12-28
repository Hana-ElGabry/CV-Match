from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


CSV_FILE_PATH = "user network.csv"  

try:

    df = pd.read_csv(CSV_FILE_PATH)
    print("CSV file loaded successfully!")
except Exception as e:
    print(f"Error loading CSV file: {e}")
    df = pd.DataFrame(columns=["Name", "Age", "Email"])  

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users"""
    if df.empty:
        return jsonify({"message": "No users found."}), 200

    try:

        users = df.to_dict(orient='records')
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['GET'])
def search_user():
    """Search for a user by name"""
    if df.empty:
        return jsonify({"message": "No users found."}), 200


    username = request.args.get('username', '')

    if not username:
        return jsonify({"error": "Please provide a username to search for."}), 400

    try:

        result = df[df.apply(lambda row: row.astype(str).str.contains(username, case=False).any(), axis=1)]

        if not result.empty:
            return result.to_json(orient='records'), 200
        else:
            return jsonify({"message": f"User '{username}' not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the CSV and DataFrame"""
    global df  
    try:

        name = request.json.get("name")
        age = request.json.get("age")
        email = request.json.get("email")

        if not name or not email:
            return jsonify({"error": "Name and email are required."}), 400


        new_user = {"Name": name, "Age": age, "Email": email}
        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)


        df.to_csv("user network.csv", index=False)

        return jsonify({"message": "User added successfully.", "user": new_user}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/remove_user', methods=['DELETE'])
def remove_user():
    """Remove a user from the CSV and DataFrame"""
    global df
    try:
        email = request.json.get("email")

        if not email:
            return jsonify({"error": "Email is required to remove a user."}), 400

        if email not in df['Email'].values:
            return jsonify({"message": f"User with email '{email}' not found."}), 404

        df = df[df['Email'] != email]

        df.to_csv("user network.csv", index=False)

        return jsonify({"message": "User removed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
    