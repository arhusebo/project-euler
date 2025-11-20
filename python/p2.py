def f(c, p, s):
    n = c+p
    even = not n%2
    sn = s+(n if even else 0)
    return f(n, c, sn) if n<4e6 else sn


print(f(1, 0, 0))
