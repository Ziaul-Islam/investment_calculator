class InvestmentCalculator:
    def __init__(self, initial_investment, rates, contribution_amount, contribution_type):
        self.initial_investment = initial_investment
        self.rates = [rate / 100 for rate in rates]
        self.contribution_amount = contribution_amount
        self.contribution_type = contribution_type

    def calculate_final_value(self):
        final_value = self.initial_investment
        contribution_per_year = self.contribution_amount * (12 if self.contribution_type == "monthly" else 1)

        for year, rate in enumerate(self.rates):
            # Add the annual contribution
            final_value += contribution_per_year
            # Apply the annual return rate for that specific year
            final_value *= (1 + rate)
            
        return round(final_value, 2)
