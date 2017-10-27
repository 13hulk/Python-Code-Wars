def unique(integers):
    a = []
    for i in integers:
        if i not in a:
            a.append(i)    
    return a
