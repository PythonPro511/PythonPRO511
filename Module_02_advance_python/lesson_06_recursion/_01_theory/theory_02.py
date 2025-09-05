# решение через цикл
def calc_sum(n):
    res = 0
    while True:
        if n == 0:
            break
        res += n
        n -= 1
    return res


# решение через рекурсию

def calc_sum_recursive(n):
    if n == 1:
        return 1
    return n + calc_sum_recursive(n - 1)


"""
1) 4 + calc_sum_recursive(3)
2) 4 + (3 + calc_sum_recursive(2))
3) 4 + (3 + (2 + calc_sum_recursive(1))
4) 4 + (3 + (2 + (1)))
5) 10 # возвращаем сумму: 4 + 3 + 2 + 1 = 10
"""

if __name__ == '__main__':
    print(calc_sum(5))
    print(calc_sum_recursive(5))
