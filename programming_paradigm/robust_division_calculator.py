def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is: {float(numerator) / float(denominator)}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        

    except ValueError:
        if type(numerator) == str or type(denominator) == str:
            return "Error: Please enter numeric values only."



