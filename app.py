from flask import Flask, render_template, request

app = Flask(__name__)

# 🧮 Home - Basic Calculator
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

# 🔬 Scientific Calculator (Placeholder)
@app.route("/scientific")
def scientific():
    return render_template("scientific.html")

# 📈 Simple Interest Calculator
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

# ⏳ Future Money Value (Placeholder)
@app.route("/money-value", methods=["GET", "POST"])
def money_value():
    result = ""
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            inflation = float(request.form["inflation"])
            years = float(request.form["years"])
            future_value = amount / ((1 + (inflation / 100)) ** years)
            result = f"Estimated future value: ₹{future_value:.2f}"
        except:
            result = "Invalid Input"
    return render_template("money_value.html", result=result)

# 🌍 Currency Comparison (Placeholder)
@app.route("/currency-compare", methods=["GET", "POST"])
def currency_compare():
    result = ""
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            rate = float(request.form["rate"])
            converted = amount * rate
            result = f"Converted amount: ₹{converted:.2f}"
        except:
            result = "Invalid Input"
    return render_template("currency_compare.html", result=result)

# 📝 Bill To-Do List (Placeholder)
@app.route("/todo", methods=["GET", "POST"])
def todo():
    # You can later add file or session-based todo saving here
    return render_template("todo.html")

# 💳 EMI Calculator (Placeholder)
@app.route("/emi", methods=["GET", "POST"])
def emi():
    result = ""
    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            rate = float(request.form["rate"]) / (12 * 100)
            months = int(request.form["months"])
            emi = (principal * rate * ((1 + rate)*months)) / (((1 + rate)*months) - 1)
            result = f"Monthly EMI: ₹{emi:.2f}"
        except:
            result = "Invalid Input"
    return render_template("emi.html", result=result)

# 🚀 Run Server
if __name__ == "_main_":
    app.run(debug=True)