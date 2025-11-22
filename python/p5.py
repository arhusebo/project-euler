from itertools import count

def p(fmax):
    return next(filter(lambda n: not any((n%x for x in range(2, fmax+1))),
                       count(fmax, fmax)))

print(p(20))
