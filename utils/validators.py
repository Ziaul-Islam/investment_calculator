def is_positive_number(value):
    try:
        return float(value) > 0
    except ValueError:
        return False
