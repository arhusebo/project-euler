from functools import partial


a = sum(set().union(*map(partial(range, 0, 1000), (3, 5))))


print(a)
