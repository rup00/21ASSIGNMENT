def reverseEven(N): 
  
    if N % 2 != 0: 
        return
  
    if N <= 0: 
        return
  
    print(N, end = ' ') 
    reverseEven(N - 2) 
  

N = 10
reverseEven(N)