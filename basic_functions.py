"""Practice with basic testing."""

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by a zero")
    return x / y

def floor_divide(x,y):
    """Floor division to round result down."""
    if y == 0:
        raise ValueError("Cannot divide by a zero")
    return x // y

def mod(x,y):
    return x % y

