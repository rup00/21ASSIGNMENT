def print_odd_natural_numbers_in_reverse_order(n):
    if n <= 0:
        return
    print(n)
    print_odd_natural_numbers_in_reverse_order(n - 2)