from flask import Flask, jsonify, request

task6 = Flask(__name__)

@task6.route("/",methods=['GET','POST'])
def home():
    return jsonify({"Message":"Welcome to Square of a Number by POST method! Go to /square/{number}"})

@task6.route("/square/<int:n>",methods=['POST'])
def getsquare(n):
    return jsonify({f"Square of {n}" : n**2})

    
if __name__ == "__main__":
    task6.run(debug=True)