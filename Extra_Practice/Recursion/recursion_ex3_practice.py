"""
3. Recursive Lines
    Write a recursive function that accepts an integer argument, n. The function should display
    n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
    showing 2 asterisks, up to the nth line which shows n asterisks.
"""

def rec_lines(n):
    if n > 1:
        rec_lines(n-1)
    print("*" * n)
    
rec_lines(6)