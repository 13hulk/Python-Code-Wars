pairs = [(1, 'one',55), (3, 'two',66,33), (2, 'three',2), (4, 'four',1,1)]
#pairs.sort()
print(pairs)
pairs.sort(key=lambda x : x[2])
print(pairs)