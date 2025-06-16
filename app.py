from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ------------------ MongoDB Setup ------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["calculator_app"]
todo_collection = db["todo_tasks"]

# ------------------ Basic Calculator ------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            expression = request.form['expression']
            result = eval(expression)
        except:
            result = "Invalid Expression"
    return render_template('index.html', result=result)

# ------------------ Simple Interest ------------------
@app.route('/simple-interest', methods=['GET', 'POST'])
def simple_interest():
    result = None
    if request.method == 'POST':
        try:
            p = float(request.form['principal'])
            r = float(request.form['rate'])
            t = float(request.form['time'])
            result = f"Simple Interest: {(p * r * t) / 100:.2f}"
        except:
            result = "Invalid Input"
    return render_template('simple_interest.html', result=result)

# ------------------ Currency Converter ------------------
@app.route('/currency', methods=['GET', 'POST'])
def currency():
    result = None
    if request.method == 'POST':
        try:
            amt = float(request.form['amount'])
            rate = float(request.form['rate'])
            result = f"Converted Amount: {amt * rate:.2f}"
        except:
            result = "Invalid Input"
    return render_template('currency.html', result=result)

# ------------------ Future Value Calculator ------------------
@app.route('/money-value', methods=['GET', 'POST'])
def money_value():
    result = None
    if request.method == 'POST':
        try:
            amt = float(request.form['amount'])
            rate = float(request.form['inflation']) / 100
            yrs = float(request.form['years'])
            future = amt * ((1 + rate) ** yrs)
            result = f"Future Value: {future:.2f}"
        except:
            result = "Invalid Input"
    return render_template('money_value.html', result=result)

# ------------------ EMI Calculator ------------------
@app.route('/emi', methods=['GET', 'POST'])
def emi():
    result = None
    if request.method == 'POST':
        try:
            p = float(request.form['principal'])
            r = float(request.form['rate']) / 12 / 100
            n = int(request.form['months'])
            emi = (p * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
            result = f"Monthly EMI: {emi:.2f}"
        except:
            result = "Invalid Input"
    return render_template('emi.html', result=result)

# ------------------ To-Do List with MongoDB ------------------
@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todo_collection.insert_one({'task': task})
        return redirect(url_for('todo'))
    tasks = list(todo_collection.find())
    return render_template('todo.html', tasks=tasks)

@app.route('/delete-task/<task_id>')
def delete_task(task_id):
    todo_collection.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('todo'))

# ------------------ Scientific Calculator ------------------
@app.route('/scientific')
def scientific():
    return render_template('scientific.html')

# ------------------ 404 Error Handler ------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
7
# ------------------ Run Flask App ------------------
if __name__ == '_main_':
    app.run(debug=True)