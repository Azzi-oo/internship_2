def is_pal(n):
    n = ''.join(c for c in n if c.isalnum())
    return n == n[::-1]
