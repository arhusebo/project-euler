from math import sqrt

# a + b + c = 1000
# a < b < c
# a² + b² = c²

# ex.
# 200 + 300 + 500 = 1000
# a < b < c
# 200² + 300² = 40000 + 90000 = 130000 != 250000


def f(n):
    for a in range(1, n):
        for b in range(a, n-a):
            for c in range(b, int(sqrt(a**2+b**2))+1):
                if a+b+c==n and a**2+b**2==c**2:
                    return a, b, c

a, b, c = f(1000)
print(f"{a}*{b}*{c}={a*b*c}")
