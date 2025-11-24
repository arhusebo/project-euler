from math import sqrt
from itertools import count, islice


def primegen():
    yield 2
    for i in count(3, 2):
        if not any((i%j==0 for j in range(3, int(sqrt(i))+1, 2))):
            yield i


def nth_prime(n):
    return next(_ for (i, _) in enumerate(primegen()) if i==n-1)


print(nth_prime(10001))

