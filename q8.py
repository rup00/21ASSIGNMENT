
def print_cube(N): 
  
    if N < 1: 
       return
  
    print(N*N*N) 
    print_cube(N-1)