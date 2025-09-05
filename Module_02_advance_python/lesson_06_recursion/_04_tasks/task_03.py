def find_value(tree: list, value) -> bool:
    if not isinstance(tree, list):
        return tree == value

    for item in tree:
        if find_value(item, value):
            return True

    return False


if __name__ == '__main__':
    data_tree = [1, [2, [3, 4], 5], [6, 7]]
    print(find_value(data_tree, 5))
    print(find_value(data_tree, 8))
