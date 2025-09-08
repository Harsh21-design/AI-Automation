from flask import Flask, request, jsonify

task4= Flask(__name__)
secret_token = "mysecretkey123"

@task4.route("/secure")
def secure():
    token = request.headers.get("Authorization")
    if token == f"Bearer {secret_token}":
        return jsonify({"Data": "This is protected data!"})
    return jsonify({"error": "Unauthorized"}), 401

@task4.route("/",methods=['GET'])
def home():
    return jsonify({"Message":"Welcome!."})


if __name__ == "__main__":
    task4.run(debug=True)