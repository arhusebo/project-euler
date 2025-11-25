from math import sqrt
from itertools import count, takewhile


def primegen():
    yield 2
    for i in count(3, 2):
        if not any((i%j==0 for j in range(3, int(sqrt(i))+1, 2))):
            yield i


a = sum(takewhile(2e6.__ge__, primegen()))

print(a)
