import enum

class Account(enum.Enum):
    KZT: str = 'KZT'
    RUB: str = 'RUB'
    USD: str = 'USD'
    EUR: str = 'EUR'

class BankAccount(object):
    name: str
    surname: str
    money: float
    currency: Account

    def __init__(self, name, surname, money, currency) -> None:
        self.name = name
        self.surname = surname
        self.money = money
        self.currency = currency

    def addToBankAccount(self, money) -> None:
        self.money += money

    def substractFromBankAccount(self, money) -> None:
        self.money -= money

    def moneyConversion(self, currency) -> None:
        match self.currency.value:
            case 'KZT':
                match currency:
                    case 'RUB':
                        self.money *= 0.13
                        self.currency = Account.RUB
                    case 'USD':
                        self.money *= 0.0021
                        self.currency = Account.USD
                    case 'EUR':
                        self.money *= 0.002
                        self.currency = Account.EUR
            case 'RUB':
                match currency:
                    case 'KZT':
                        self.money *= 7.53
                        self.currency = Account.KZT
                    case 'USD':
                        self.money *= 0.016
                        self.currency = Account.USD
                    case 'EUR':
                        self.money *= 0.015
                        self.currency = Account.EUR
            case 'USD':
                match currency:
                    case 'KZT':
                        self.money *= 470.69
                        self.currency = Account.KZT
                    case 'RUB':
                        self.money *= 62.52
                        self.currency = Account.RUB
                    case 'EUR':
                        self.money *= 0.95
                        self.currency = Account.EUR
            case 'EUR':
                match currency:
                    case 'KZT':
                        self.money *= 496.17
                        self.currency = Account.KZT
                    case 'RUB':
                        self.money *= 65.90
                        self.currency = Account.RUB
                    case 'USD':
                        self.money *= 1.05
                        self.currency = Account.USD

    def toString(self) -> None:
        print('*' * 30)
        print(f'Имя пользователя: {self.name}')
        print(f'Фамилия пользователя: {self.surname}')
        print(f'Деньги пользователя: {self.money}')
        print(f'Валюта пользователя: {self.currency.value}')
        print('*' * 30)

    def get_user(self) -> str:
        return f'{self.money} {self.currency.value}'

    def set_user(self, money) -> None:
        self.money = money

    def __repr__(self) -> None:
        return f'{self.name} {self.surname}'

    def __del__(self) -> None:
        print(f'Пользователь {self.name} {self.surname} удален!')

users = []
while True:
    user_main_menu = input('Выберите ваше действие: \n1.Создание пользователя \n2.Выбрать пользователя \n0.Выйти\n')
    try:
        user_main_menu = int(user_main_menu)
        if user_main_menu in (0, 1, 2):
            pass
        else:
            print('Введите число от 1 до 2, либо 0 для выхода!')
    except:
        print('Вы ввели не число!')
        continue
    match user_main_menu:
        case 1:
            user_name = input('Введите имя: ')
            user_surname = input('Введите фамилию: ')
            try:
                user_money = int(input('Введите количество денег: '))
            except:
                print('Введите числа!')
                user_money = input('Введите количество денег: ')
                while not isinstance(user_money, int):
                    try:
                        user_money = int(user_money)
                    except:
                        print('Введите числа!')
                        user_money = input('Введите количество денег: ')
            user_currency = input('Введите валюту (KZT, RUB, USD, EUR): ')
            while user_currency not in ('KZT', 'RUB', 'USD', 'EUR'):
                print('Вы ввели невозможную валюту!')
                user_currency = input('Введите валюту (KZT, RUB, USD, EUR): ')
            if user_currency == 'KZT':
                user_currency = Account.KZT
            elif user_currency == 'RUB':
                user_currency = Account.RUB
            elif user_currency == 'USD':
                user_currency = Account.USD
            elif user_currency == 'EUR':
                user_currency = Account.EUR
            user = BankAccount(user_name, user_surname, user_money, user_currency)
            users.append(user)
            print('Пользователь успешно добавлен!\n')
        case 2:
            if len(users) == 0:
                print('В банке нет пользователей!')
                continue
            for i in range (len(users)):
                print(f'{i + 1}. {users[i]}')
            try:
                user_number = int(input('Выберите пользователя по индексу: '))
            except:
                print('Введите числа!')
                user_number = input('Выберите пользователя по индексу: ')
                while not isinstance(user_number, int):
                    try:
                        user_number = int(user_number)
                    except:
                        print('Введите числа!')
                        user_number = input('Выберите пользователя по индексу: ')
            
            account = users[user_number - 1]

            while True:
                print('1 - Данные аккаунта')
                print('2 - Вывести счет')
                print('3 - Установить счет')
                print('4 - Внести деньги')
                print('5 - Снять деньги')
                print('6 - Конвертация счета')
                print('0 - Главное меню')
                menu = int(input('Выберите операцию: '))
                match menu:
                    case 1:
                        account.toString()
                    case 2:
                        print(account.get_user())
                    case 3:
                        account.set_user(int(input('Введите количество денег: ')))
                    case 4:
                        input_money = int(input())
                        account.addToBankAccount(input_money)
                    case 5:
                        input_money = int(input())
                        account.substractFromBankAccount(input_money)
                    case 6:
                        input_currency = input()
                        account.moneyConversion(input_currency)
                    case 0:
                        break
                    case other:
                        print('Введите число от 1 до 6, либо 0 для выхода в Главное меню!')
        case 0:
            break
