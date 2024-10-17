def calculate_investment(initial_investment, contribution_type, contribution_amount, rates):
    total = initial_investment
    for rate in rates:
        total += (contribution_amount * 12 if contribution_type == 'monthly' else contribution_amount)
        total *= (1 + rate / 100)
    return round(total, 2)
