def swap(st):
    return ''.join( i.upper() if i in 'aeiou' else i for i in st)
