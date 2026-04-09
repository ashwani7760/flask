from flask import Flask ,request ,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/discount",methods = ["POST"])
def discount():
    values = request.form.getlist("values")

    total_sum = sum(int(v) for v in values)

    if total_sum <= 1000:
        total = total_sum * 0.90
    elif total_sum <= 2000:
        total = total_sum * 0.80
    else:
        total = total_sum * 0.70

    return {"amount payable after discount": total}

if __name__ =="__main__":
    app.run()