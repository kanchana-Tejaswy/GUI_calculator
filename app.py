from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scientific')
def scientific():
    return render_template('scientific.html')

@app.route('/simple-interest', methods=['GET', 'POST'])
def simple_interest():
    result = ""
    if request.method == 'POST':
        p = float(request.form['principal'])
        r = float(request.form['rate'])
        t = float(request.form['time'])
        si = (p * r * t) / 100
        result = f"Simple Interest: ₹{si:.2f}"
    return render_template('simple_interest.html', result=result)

@app.route('/money-value', methods=['GET', 'POST'])
def money_value():
    result = ""
    if request.method == 'POST':
        past_value = float(request.form['amount'])
        inflation = float(request.form['inflation'])
        years = int(request.form['years'])
        future_value = past_value * ((1 + inflation / 100) ** years)
        result = f"Future Money Value: ₹{future_value:.2f}"
    return render_template('money_value.html', result=result)

@app.route('/currency-compare', methods=['GET', 'POST'])
def currency_compare():
    result = ""
    if request.method == 'POST':
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = float(request.form['amount'])
        res = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        data = res.json()
        rate = data['rates'][to_currency]
        result = f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}"
    return render_template('currency_compare.html', result=result)

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    tasks = []
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('todo.html', tasks=tasks)

@app.route('/emi', methods=['GET', 'POST'])
def emi():
    result = ""
    if request.method == 'POST':
        p = float(request.form['principal'])
        r = float(request.form['rate']) / (12 * 100)
        n = int(request.form['months'])
        emi = (p * r * ((1 + r)*n)) / (((1 + r)*n) - 1)
        result = f"Monthly EMI: ₹{emi:.2f}"
    return render_template('emi.html', result=result)

if __name__ == '_main_':
    app.run(debug=True)