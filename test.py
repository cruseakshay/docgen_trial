def pow(a, b):
    """
    Calculates the power of a number.

    Args:
        a (int or float): The base number.
        b (int or float): The exponent.

    Returns:
        int or float: The result of raising a to the power of b.
    """
    return a**b


def mul(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b


def sub(a, b):
    """
    Subtracts two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference between a and b.
    """
    return a - b


def mod(a, b):
    """
    Calculates the modulus of two numbers.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The remainder when a is divided by b.
    """
    return a % b


def customFunc(a, b):
    """
    Performs a custom calculation on two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of the custom calculation, which is obtained by multiplying a by 3, adding the square root of b, and then adding 8.
    """
    return (a * 3) + (b**0.5) + 8


def func1(p_list):
    return sum([ele for ele in p_list if ele % 2 == 0])
