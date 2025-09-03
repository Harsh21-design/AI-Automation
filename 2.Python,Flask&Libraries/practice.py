from flask import Flask

practice = Flask(__name__)

@practice.route("/",methods=['GET'])
def home():
    return f'This is a basic Flask Api Practice Problem'

if __name__ == "__main__":
    practice.run(debug=True)