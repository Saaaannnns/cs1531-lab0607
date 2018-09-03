from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator



@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        initial = float(request.form["initial"])
        rate = float(request.form["rate"])
        time = float(request.form["time"])
        calc = Calculator(initial,rate)
        total = float(calc.total_interest(time))
        return render_template('interest_form.html', calc_total=True, total=total)
    return render_template('interest_form.html', calc_total=True, total=0)


@app.route('/time', methods=['POST', 'GET'])
def time_interest():
    time_final = 0
    if request.method == 'POST':
        initial = float(request.form["initial"])
        rate = float(request.form["rate"])
        time = float(request.form["time"])
        calc = Calculator(initial,rate)
        total = float(calc.total_interest(time))
        time_final = float(calc.time_required(total))
    
    return render_template('time.html', calc_time_final=True, time_final=time_final)

@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html')
