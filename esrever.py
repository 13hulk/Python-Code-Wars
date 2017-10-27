def esrever(string):  
    return ' '.join( i for i in [s[::-1] for s in string[:-1].split()][::-1] ) + string[-1] if string else ''
