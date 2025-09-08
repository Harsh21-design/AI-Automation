from flask import Flask, jsonify
import requests

task5 = Flask(__name__)

@task5.route("/",methods=['GET'])
def home():
    return jsonify({"Message":"Welcome! Go to /user/{username}"})


@task5.route("/user/<username>",methods=['GET'])
def getuserifgo(username):
    url = f"https://api.github.com/users/{username}"  
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "User not found!"}),404


if __name__ == "__main__":
    task5.run(debug=True)