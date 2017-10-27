def sum_times_tables(table,a,b):
    return sum( i*j for i in table for j in range(a, b+1) )
