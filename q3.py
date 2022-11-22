
def printNoddNumbers(n): 
    if n%2!=0: 
        print(n)
        printNoddNumbers(n-1) 
    else: 
        printNoddNumbers(n-1)