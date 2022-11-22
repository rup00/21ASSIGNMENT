def reverseNaturals(n): 
    if n <= 0: 
        return
    reverseNaturals(n-1) 
    print(n, end=' ')