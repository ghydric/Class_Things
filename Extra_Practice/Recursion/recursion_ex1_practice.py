"""
1. Recursive Printing
    Design a recursive function that accepts an integer argument, n, and prints the numbers 1
    up through n.
"""

def print_integer(n):
    if n > 1:
        print_integer(n - 1)
    print(n, sep=" ")

print(print_integer(5))