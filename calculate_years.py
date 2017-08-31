def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    
    years = 0
    
    while principal < desired:
        principal += (interest * principal) * (1 - tax)
        years += 1
        
    return years
