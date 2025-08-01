# robust division calculator
def safe_divide(numerator, denominator):
    """
    Perform division with error handling for zero denominator.  
    Returns 'undefined' if the denominator is zero.

    Args:
    numerator (str): The numerator input as a string.
    denominator (str): The denominator input as a string.

    Returns:
     str: The result of the division or 'undefined' if the denominator is zero. 
    """
    try:
        result = float(numerator) / float(denominator)
        return f"the result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."
