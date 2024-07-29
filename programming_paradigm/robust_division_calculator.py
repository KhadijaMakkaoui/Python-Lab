def safe_divide(numerator, denominator):
    
    try:
        result= int(numerator) / int(denominator)
        return str(result)
    except ZeroDivisionError:
        return str("division by zero!")
    except ValueError:
        return str("Non numeric inputs!")