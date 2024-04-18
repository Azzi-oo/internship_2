def count_chisla(num):
    if not isinstance(num, int):
        return "Введено не число"
    count = 0
    if num.is_digit():
        for i in str(num):
            count += 1
        return count


def count_chisla2(num):
    if not isinstance(num, int):
        return "Введено не число"

    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
