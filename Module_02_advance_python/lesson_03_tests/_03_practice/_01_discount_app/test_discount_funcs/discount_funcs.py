def calculate_discount(level, amount):
    if level == 'basic':
        return amount * 0.95
    elif level == 'silver':
        return amount * 0.9
    elif level == 'gold':
        return amount * 0.85
    else:
        raise ValueError('Unknown level')
