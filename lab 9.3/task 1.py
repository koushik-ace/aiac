"""Compute and display the sum of even and odd numbers in a list.

This script iterates through a predefined list of integers, accumulates the sum
of even numbers and the sum of odd numbers separately, and prints both totals.
"""

# Input list of integers to process
a=[1,2,3,4,5,6,7,8,9,10]

def sum_even(a):
    """Return the sum of even integers in the iterable `a`.

    Parameters:
        a: Iterable of integers to scan for even values.

    Returns:
        int: Sum of all even integers found in `a`.
    """
    sume=0
    for i in a:
        if i%2==0:
            sume=sume+i
    return sume
def sum_odd(a):
    """Return the sum of odd integers in the iterable `a`.

    Parameters:
        a: Iterable of integers to scan for odd values.

    Returns:
        int: Sum of all odd integers found in `a`.
    """
    sumo=0
    for i in a:
        if i%2!=0:
            sumo=sumo+i
    return sumo

# Print the sum of even numbers followed by the sum of odd numbers
print(sum_even(a))
print(sum_odd(a))