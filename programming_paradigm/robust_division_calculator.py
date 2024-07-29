def safe_divide(numerator, denominator):
    
    try:
        result= float(numerator) / float(denominator)
        return str(result)
    except ZeroDivisionError:
        return str("division by zero!Error: Cannot divide by zero.")
    except ValueError:
        return str("Non numeric inputs!Error: Please enter numeric values only.")