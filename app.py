from flask import Flask, render_template, request, jsonify
from calculator.investment import calculate_investment  # Updated import statement
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        initial_investment = float(request.form['initial_investment'])
        contribution_type = request.form['contribution_type']
        contribution_amount = float(request.form['contribution_amount'])
        rates = [float(rate) for rate in request.form.getlist('rates[]')]

        final_value = calculate_investment(initial_investment, contribution_type, contribution_amount, rates)

        return jsonify({'success': True, 'final_value': final_value})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
