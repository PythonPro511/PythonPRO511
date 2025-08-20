class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


if __name__ == '__main__':
    s1 = Student('Иван', 16)
    s2 = Student('Иван', 16)
    s3 = Student('Мария', 15)

    print(s1 == s2)
    print(s1 == s3)
    print()
    print(s1 is s2)

    s4 = s1
    print(s1 is s4)


