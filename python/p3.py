def pfac(n, sup=1):
    if n==1: return sup
    d = next(filter(lambda d: n%d==0, range(2, int(n**0.5))), 1)
    if d==1 and n>sup: return n
    return pfac(n//d, sup)


print(pfac(600851475143))
