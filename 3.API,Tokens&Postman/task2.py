from flask import Flask, request, jsonify

task2 = Flask(__name__)

person = [
    {"id":1,"name":"Alen","age":20},
    {"id":2,"name":"Bob","age":25}
]

@task2.route("/person",methods=['GET'])
def get_request():
    return jsonify(person)

@task2.route("/person/<int:id>",methods=['POST'])
def post_request(id):
    newperson = {
        "id":request.json['id'],
        "name":request.json['name'],
        "age":request.json['age']
    }
    person.append(newperson)
    return jsonify({'Message':'Person added successfully.'})


if __name__ == "__main__":
    task2.run(debug=True)