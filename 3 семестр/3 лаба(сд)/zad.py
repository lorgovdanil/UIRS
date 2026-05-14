def f(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    bd = f(b, d)
    ac = f(a, c)
    abcd = f((b + a), (d + c))

    s =  (ac * 10**(2 * n2)) + ((abcd - ac - bd) * 10**n2) + bd
    return s

x = 123456
y = 987
s = f(x, y)
print(f"Результат: {s}")