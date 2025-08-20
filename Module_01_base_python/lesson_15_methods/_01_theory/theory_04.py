class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"{self.owner} пополнил счёт на {amount}. Новый баланс: {self.balance}")
        else:
            print(f'Ошибка: Неверная сумма.')

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Процентная ставка изменена на {cls.interest_rate * 100:.2f}%")

    @staticmethod
    def is_valid_amount(amount):
        # if amount > 0:
        #     return True
        return amount > 0


if __name__ == '__main__':
    account_ivan = BankAccount('Иван', 1000)
    # работа с экземпляром
    account_ivan.deposit(-200)
    account_ivan.deposit(500)
    print(account_ivan.balance)

    # работа с классом
    BankAccount.set_interest_rate(0.07)
    print(BankAccount.interest_rate)

    # использование staticmethod вне класса
    print(BankAccount.is_valid_amount(200))

    ivan_sum = float(input('Введите сумму для пополнения: '))
    if BankAccount.is_valid_amount(ivan_sum):
        account_ivan.deposit(ivan_sum)
    else:
        print("Отказ из основного кода")
