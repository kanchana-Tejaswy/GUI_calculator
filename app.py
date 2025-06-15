from flask import Flask, render_template, request

app = Flask(__name__)

# ------------------ BASIC CALCULATOR ------------------
@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ''
    result = ''
    if request.method == 'POST':
        button = request.form['btn']
        expression = request.form.get('expression', '')

        if button == 'C':
            expression = ''
        elif button == '=':
            try:
                result = str(eval(expression))
                expression = result
            except:
                result = 'Error'
                expression = ''
        else:
            expression += button
            result = expression

    return render_template('index.html', result=result)


# ------------------ SCIENTIFIC CALCULATOR ------------------
@app.route('/scientific')
def scientific():
    return render_template('scientific.html')


# ------------------ SIMPLE INTEREST ------------------
@app.route('/simple-interest', methods=['GET', 'POST'])
def simple_interest():
    result = None
    if request.method == 'POST':
        try:
            p = float(request.form['principal'])
            r = float(request.form['rate'])
            t = float(request.form['time'])
            si = (p * r * t) / 100
            result = f"Simple Interest = ₹{si:.2f}"
        except:
            result = "Invalid Input"
    return render_template('simple_interest.html', result=result)


# ------------------ MONEY VALUE ------------------
@app.route('/money-value')
def money_value():
    return render_template('money_value.html')


# ------------------ CURRENCY COMPARISON ------------------
@app.route('/currency-compare')
def currency_compare():
    return render_template('currency_compare.html')


# ------------------ TO-DO BILL LIST ------------------
@app.route('/todo')
def todo():
    return render_template('todo.html')


# ------------------ EMI CALCULATOR ------------------
@app.route('/emi')
def emi():
    return render_template('emi.html')


# ------------------ RUN THE APP ------------------
if __name__ == '_main_':
    app.run(debug=True)