
def printEven(n): 
    if n % 2 == 0: 
        print(n, end = " ") 
    if n > 1: 
        printEven(n - 1)