"""Simple interactive calculator.

This module provides basic arithmetic operations and a simple
command-line interface to select an operation and compute the result
for two user-provided numbers.

Notes
-----
- Supported operations: addition, subtraction, multiplication, division,
  modulus, and exponentiation.
- The interactive portion reads from standard input and prints results
  to standard output.
"""

def calculater_add(a,b):
    """Add two numbers.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The sum of ``a`` and ``b``.
    """
    return a+b
def calculater_sub(a,b):
    """Subtract two numbers.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The result of ``a - b``.
    """
    return a-b
def calculater_mul(a,b):
    """Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First factor.
    b : int or float
        Second factor.

    Returns
    -------
    int or float
        The product ``a * b``.
    """
    return a*b
def calculater_div(a,b):
    """Divide two numbers.

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.

    Returns
    -------
    float
        The quotient ``a / b``.

    Raises
    ------
    ZeroDivisionError
        If ``b`` is zero.
    """
    return a/b
def calculater_mod(a,b):
    """Compute the modulus of two numbers.

    Parameters
    ----------
    a : int
        Dividend.
    b : int
        Divisor.

    Returns
    -------
    int
        The remainder of ``a % b``.

    Raises
    ------
    ZeroDivisionError
        If ``b`` is zero.
    """
    return a%b
def calculater_pow(a,b):
    """Raise a number to a power.

    Parameters
    ----------
    a : int or float
        Base.
    b : int or float
        Exponent.

    Returns
    -------
    int or float
        The value of ``a ** b``.
    """
    return a**b
print("select the operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. modulus")
print("6. power")
choice = int(input("enter the choice:"))
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
if choice == 1:
    print(calculater_add(a,b))
elif choice == 2:
    print(calculater_sub(a,b))
elif choice == 3:
    print(calculater_mul(a,b))
elif choice == 4:
    print(calculater_div(a,b))
elif choice == 5:
    print(calculater_mod(a,b))
elif choice == 6:
    print(calculater_pow(a,b))