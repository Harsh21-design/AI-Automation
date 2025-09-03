from flask import Flask, render_template, request

Task5 = Flask(__name__)
@Task5.route("/",methods=['GET','POST'])
def greet():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return render_template("greeting.html", name=first_name, lname=last_name)
    return render_template("form.html")

if __name__ == "__main__":
    Task5.run(debug=True)