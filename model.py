def predict_sales(advertising_budget):
    if advertising_budget < 0:
        raise ValueError("Budget cannot be negative")

    return advertising_budget * 2.5
