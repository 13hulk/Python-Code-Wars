def find_short(s):
    string = s.split(' ')
    
    short = string[0]
    
    for i in string:
        if len(i) < len(short):
            short = i
    return len(short)
