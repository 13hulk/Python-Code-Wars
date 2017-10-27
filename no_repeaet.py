def no_repeat(string):
    return [i for i in string if string.count(i) == 1][0]
