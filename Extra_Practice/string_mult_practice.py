def display_happy(n):
    if n > 1:
        display_happy(n-1)
    print("happy" * n)

display_happy(4)