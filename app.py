from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- Home: Basic Calculator ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression)
        except Exception:
            result = "Invalid Expression"
    return render_template("index.html", result=result)

# ---------------- Simple Interest ----------------
@app.route("/simple-interest", methods=["GET", "POST"])
def simple_interest():
    result = None
    if request.method == "POST":
        try:
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            si = (p * r * t) / 100
            result = f"Simple Interest: ₹{si:.2f}"
        except Exception:
            result = "Invalid Input"
    return render_template("simple_interest.html", result=result)

# ---------------- Currency Comparison ----------------
@app.route("/currency-compare", methods=["GET", "POST"])
def currency_compare():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            rate = float(request.form["rate"])
            converted = amount * rate
            result = f"Converted Amount: ₹{converted:.2f}"
        except Exception:
            result = "Invalid Input"
    return render_template("currency.html", result=result)

# ---------------- Future Money Value ----------------
@app.route("/money-value", methods=["GET", "POST"])
def money_value():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            inflation = float(request.form["inflation"])
            years = float(request.form["years"])
            future_value = amount / ((1 + inflation / 100) ** years)
            result = f"Estimated Future Value: ₹{future_value:.2f}"
        except Exception:
            result = "Invalid Input"
    return render_template("money_value.html", result=result)

# ---------------- EMI Calculator ----------------
@app.route("/emi", methods=["GET", "POST"])
def emi():
    result = None
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            annual_rate = float(request.form["rate"]) / (12 * 100)
            months = int(request.form["months"])
            emi = (principal * annual_rate * (1 + annual_rate) ** months) / ((1 + annual_rate) ** months - 1)
            result = f"Monthly EMI: ₹{emi:.2f}"
        except Exception:
            result = "Invalid Input"
    return render_template("emi.html", result=result)

# ---------------- To-Do List ----------------
tasks = []

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("todolist.html", tasks=tasks)

@app.route("/delete-task/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("todo"))

# ---------------- Scientific Calculator ----------------
@app.route("/scientific")
def scientific():
    return render_template("scientific.html")

# ---------------- 404 Error ----------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# ---------------- Run Server ----------------
if __name__ == "_main_":
    app.run(debug=True)