from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🔢 Basic Calculator
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            expression = request.form["expression"]
            result = eval(expression)
        except:
            result = "Invalid Expression"
    return render_template("index.html", result=result)

# 🧪 Scientific Calculator (Placeholder Page)
@app.route("/scientific")
def scientific():
    return render_template("scientific.html")

# 📊 Simple Interest Calculator
@app.route("/simple-interest", methods=["GET", "POST"])
def simple_interest():
    result = ""
    if request.method == "POST":
        try:
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            si = (p * r * t) / 100
            result = f"Simple Interest: ₹{si:.2f}"
        except:
            result = "Invalid Input"
    return render_template("simple_interest.html", result=result)

# 💸 Currency Comparison
@app.route("/currency-compare", methods=["GET", "POST"])
def currency_compare():
    result = ""
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            rate = float(request.form["rate"])
            converted = amount * rate
            result = f"Converted Amount: ₹{converted:.2f}"
        except:
            result = "Invalid Input"
    return render_template("currency_compare.html", result=result)

# 📉 Money Value (Future Value Estimation)
@app.route("/money-value", methods=["GET", "POST"])
def money_value():
    result = ""
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            inflation = float(request.form["inflation"])
            years = float(request.form["years"])
            future_value = amount / ((1 + (inflation / 100)) ** years)
            result = f"Estimated Value in {years} years: ₹{future_value:.2f}"
        except:
            result = "Invalid Input"
    return render_template("money_value.html", result=result)

# 🧾 EMI Calculator
@app.route("/emi", methods=["GET", "POST"])
def emi():
    result = ""
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            rate = float(request.form["rate"]) / (12 * 100)  # monthly rate
            months = int(request.form["months"])
            emi = (principal * rate * (1 + rate)*months) / ((1 + rate)*months - 1)
            result = f"Monthly EMI: ₹{emi:.2f}"
        except:
            result = "Invalid Input"
    return render_template("emi.html", result=result)

# ✅ Bill To-Do List
tasks = []

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template("todo.html", tasks=tasks)

@app.route("/delete-task/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("todo"))

# 🚀 Run the App
if __name__ == "_main_":
    app.run(debug=True)