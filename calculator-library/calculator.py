"""Small calculator library with basic numeric operations."""
import math

def _check_number(value, name="value"):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an int or float")
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value

def add(a, b):
    return _check_number(a, "a") + _check_number(b, "b")

def subtract(a, b):
    return _check_number(a, "a") - _check_number(b, "b")

def multiply(a, b):
    return _check_number(a, "a") * _check_number(b, "b")

def divide(a, b):
    a, b = _check_number(a, "a"), _check_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def square(a):
    a = _check_number(a, "a")
    return a * a

if __name__ == "__main__":
    print(add(5, 3))
    print(divide(10, 2))
    print(square(4))
