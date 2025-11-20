import math
import functools
import itertools


def reverse_digits_old(number: int, base=10) -> int:
    pw = functools.partial(pow, base)
    lg = lambda x: math.log(x, base)

    n_digits = int(lg(number))+1
    digits = []
    for n in range(1, n_digits+1):
        high_end = number//pw(n)*pw(n)
        low_end = sum((digits[j]*pw(j) for j in range(n-1)))
        dig = (number-high_end-low_end)//pw(n-1)
        digits.append(dig)
    return int(sum((d*pw(n_digits-i-1) for i, d in enumerate(digits))))

# >>> reverse_digits(123456789))
# 987654321
# >>> hex(reverse_digits(0xabcdef, base=16)))
# 0xfedcba


def digit_count(n, base=10):
    return int(math.log(n, base))+1


def digits(n, base=10):
    digs = digit_count(n, base)
    if digs==1: yield n
    else:
        d = n//pow(base, digs-1)
        yield d
        
        low_end = n-(d*pow(base, digs-1))
        if low_end>0:
            digs_remain = digit_count(low_end, base)
            yield from (0 for _ in range(digs-1-digs_remain))
            yield from digits(low_end)
        else:
            yield 0


def reverse_digits(num, base=10):
    digits_reversed = [d for d in digits(num, base)][::-1]
    bases = range(len(digits_reversed), 0, -1)
    return sum((pow(base, b-1)*d for b, d in zip(bases, digits_reversed)))


def palindrome(n, base=10):
    high = base**(n)-1
    low = base**(n-1)
    combos = itertools.combinations(range(high, low-1, -1), 2)
    return max(filter(lambda prod: prod==reverse_digits(prod, base),
                      (a*b for a, b in combos)))


print([d for d in digits(1230004560)])
print(reverse_digits(1230004560))
print(palindrome(3))
