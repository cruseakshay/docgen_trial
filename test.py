def sum_even(p_list):
    """
    Calculates the sum of all even numbers in a given list.

    Args:
        p_list (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    return sum([ele for ele in p_list if ele % 2 == 0])
