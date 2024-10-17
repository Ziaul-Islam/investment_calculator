from flask import Flask, render_template, request
from calculator.investment import InvestmentCalculator
from utils.validators import is_positive_number

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form data
        initial_investment = float(request.form['initial_investment'])
        contribution_amount = float(request.form['contribution_amount'])
        contribution_type = request.form['contribution_type']
        
        # Capture all the annual return rates as a list
        rates = request.form.getlist('rates[]')
        rates = [float(rate) for rate in rates if is_positive_number(rate)]

        # Input validation
        if not (is_positive_number(initial_investment) and is_positive_number(contribution_amount)):
            return render_template('index.html', error="All inputs must be positive numbers.")
        
        if len(rates) == 0:
            return render_template('index.html', error="Please provide at least one annual return rate.")

        # Perform calculation
        calculator = InvestmentCalculator(initial_investment, rates, contribution_amount, contribution_type)
        final_value = calculator.calculate_final_value()

        # Pass the result to the result page
        return render_template('result.html', final_value=final_value)

    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter valid numbers.")

if __name__ == '__main__':
    app.run(debug=True)
