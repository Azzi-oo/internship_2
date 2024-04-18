def cikl_for(n):
    zero = 0
    for i in range(2, n+1, 2):
        zero += i
    print(zero)


def cikl_while(n):
    zero = 0
    i = 2
    while i <= n:
        zero += i
        i += 2
    return zero
