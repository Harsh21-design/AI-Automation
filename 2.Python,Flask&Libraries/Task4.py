from flask import Flask, render_template, request

Task4 = Flask(__name__)
@Task4.route("/",methods=['GET','POST'])
def formpage():
    if request.method=="POST":
        username = request.form['name']
        return render_template("hello.html", name=username)
    return render_template("index.html")

if __name__ == "__main__":
    Task4.run(debug=True)