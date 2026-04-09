from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return "welcome ashwani"

# methods get post
@app.route("/calculator" ,methods = ["GET","POST"])
def calculator():
    if request.method == "POST":
        # operation = request.json["operation"]
        # n1 = request.json["n1"]
        # n2 = request.json["n2"]
        operation = request.form.get("operation")
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        if operation == "add":
            result = n1 + n2
        elif operation == "mul":
            result = n1 * n2
        elif operation == "sub":
            result = n1 - n2
        elif operation == "div":
            result = n1 / n2
        elif operation == "rem":
            result = n1 % n2
        return render_template("result.html",result= result)

if __name__ == "__main__":
    app.run(  )