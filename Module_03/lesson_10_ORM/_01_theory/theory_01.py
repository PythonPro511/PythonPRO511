class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User(1, "Алиса", 25)
    print(user.name)
