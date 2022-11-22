
def print_n_multiples(num, n): 
    if n <= 0: 
        return
    print(num, end = ' ') 
    print_n_multiples(num, n - 1)