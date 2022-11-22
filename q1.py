def print_natural_numbers(n):
    if n <= 0:
        return
    print(n)
    print_natural_numbers(n - 1)