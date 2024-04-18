def func(str):
    revrse_str = ''
    index = len(str) - 1
    while index >= 0:
        revrse_str += str[index]
        index -= 1
    return revrse_str
