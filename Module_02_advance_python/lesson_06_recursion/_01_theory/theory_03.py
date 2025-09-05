def count_workers(sp):
    res = 0
    for item in sp:
        if isinstance(item, int):
            res += item
        else:
            res += count_workers(item)
    return res


if __name__ == '__main__':
    count_angola = 18
    count_new_york = [20, [10, 7]]
    count_chicago = 15
    count_usa = [count_new_york, count_chicago]
    count_all = [count_angola, count_usa]
    print(count_all)
    print(count_workers(count_all))
