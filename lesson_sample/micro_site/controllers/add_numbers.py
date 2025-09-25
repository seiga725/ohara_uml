from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            result = num1 + num2
        except ValueError:
            result = "整数を入力してください"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
