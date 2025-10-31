"""
Проблема ромбов при множественном наследовании
"""
class A:
    def __init__(self):
        print('class - A')


class B(A):
    def __init__(self):
        print('class - B from: ')
        super().__init__()


class C(A):
    def __init__(self):
        print('class - C from: ')
        super().__init__()


# class D(C, A):
#     def __init__(self):
#         print('class D from: ')
#         super().__init__()
#
#
# class D(B, C):
#     def __init__(self):
#         print('class D from: ')
#         super().__init__()
#
#
class DB(B):
    def __init__(self):
        print('class D from: ')
        super().__init__()


class DC(C):
    def __init__(self):
        print('class D from: ')
        super().__init__()


if __name__ == '__main__':
    # d = D()
    print()
    db = DB()
