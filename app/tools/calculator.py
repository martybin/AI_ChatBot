import math
import sympy as sp
from langchain.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers and return the result."""
    return a - b

@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b

@tool
def power(a: float, b: float) -> float:
    """Raise a to the power of b and return the result."""
    return a ** b

@tool
def square_root(a: float) -> float:
    """Return the square root of a number."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5

@tool
def factorial(n: int) -> int:
    """Return the factorial of a number."""
    if n < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@tool
def logarithm(a: float, base: float = 10) -> float:
    """Return the logarithm of a number with a specified base."""
    if a <= 0:
        raise ValueError("Logarithm is undefined for non-positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    return math.log(a, base)

@tool
def sine(angle: float) -> float:
    """Return the sine of an angle in degrees."""
    return math.sin(math.radians(angle))

@tool
def cosine(angle: float) -> float:
    """Return the cosine of an angle in degrees."""
    return math.cos(math.radians(angle))

@tool
def tangent(angle: float) -> float:
    """Return the tangent of an angle in degrees."""
    return math.tan(math.radians(angle))

@tool
def arcsine(value: float) -> float:
    """Return the arcsine of a value in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Arcsine is undefined for values outside the range [-1, 1].")
    return math.degrees(math.asin(value))

@tool
def arccosine(value: float) -> float:
    """Return the arccosine of a value in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Arccosine is undefined for values outside the range [-1, 1].")
    return math.degrees(math.acos(value))

@tool
def arctangent(value: float) -> float:
    """Return the arctangent of a value in degrees."""
    return math.degrees(math.atan(value))

@tool
def hyperbolic_sine(value: float) -> float:
    """Return the hyperbolic sine of a value."""
    return math.sinh(value)

@tool
def hyperbolic_cosine(value: float) -> float:
    """Return the hyperbolic cosine of a value."""
    return math.cosh(value) 

@tool
def hyperbolic_tangent(value: float) -> float:
    """Return the hyperbolic tangent of a value."""
    return math.tanh(value)

@tool
def hyperbolic_arcsine(value: float) -> float:
    """Return the hyperbolic arcsine of a value."""
    return math.asinh(value)

@tool
def hyperbolic_arccosine(value: float) -> float:
    """Return the hyperbolic arccosine of a value."""
    if value < 1:
        raise ValueError("Hyperbolic arccosine is undefined for values less than 1.")
    return math.acosh(value)

@tool
def hyperbolic_arctangent(value: float) -> float:
    """Return the hyperbolic arctangent of a value."""
    if value <= -1 or value >= 1:
        raise ValueError("Hyperbolic arctangent is undefined for values outside the range (-1, 1).")
    return math.atanh(value)

@tool
def integrate(function: str, variable: str) -> str:
    """Return the indefinite integral of a function with respect to a variable."""
    # This is a placeholder implementation. In a real scenario, you would use a symbolic math library like SymPy.
    x = sp.symbols(variable)
    try:
        func = sp.sympify(function)
        integral = sp.integrate(func, x)
        return str(integral)
    except Exception as e:
        return f"Error in integration: {e}"

@tool
def differentiate(function: str, variable: str) -> str:
    """Return the derivative of a function with respect to a variable."""
    # This is a placeholder implementation. In a real scenario, you would use a symbolic math library like SymPy.
    x = sp.symbols(variable)
    try:
        func = sp.sympify(function)
        derivative = sp.diff(func, x)
        return str(derivative)
    except Exception as e:
        return f"Error in differentiation: {e}"

@tool
def evaluate_expression(expression: str) -> float:
    """Evaluate a mathematical expression and return the result."""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise ValueError(f"Error in evaluating expression: {e}")

@tool
def solve_equation(equation: str, variable: str) -> str:
    """Solve an equation for a given variable and return the solution."""
    x = sp.symbols(variable)
    try:
        eq = sp.sympify(equation)
        solutions = sp.solve(eq, x)
        return str(solutions)
    except Exception as e:
        return f"Error in solving equation: {e}"
