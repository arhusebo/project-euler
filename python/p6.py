def diff_sumsq_sqsum(n):
    r = range(1, n+1)
    return sum(r)**2-sum((x**2 for x in r))


print(diff_sumsq_sqsum(100))
