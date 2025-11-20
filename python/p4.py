from itertools import combinations


def is_palindrome(x):
    w = str(x)
    w1 = w[:len(w)//2]
    w2 = w[len(w)//2:][::-1]
    if w1 == w2: return True
    return False


def palindrome(n):
    # largest and smallest n-digit numbers
    high = 10**(n)-1
    low = 10**(n-1)
    combos = combinations(range(high, low-1, -1), 2)
    return max(filter(is_palindrome, (a*b for a, b in combos)))


print(palindrome(3))
