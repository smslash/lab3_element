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
        print(f'?????? ????????????????????????: {self.name}')
        print(f'?????????????? ????????????????????????: {self.surname}')
        print(f'???????????? ????????????????????????: {self.money}')
        print(f'???????????? ????????????????????????: {self.currency.value}')
        print('*' * 30)

    def get_user(self) -> str:
        return f'{self.money} {self.currency.value}'

    def set_user(self, money) -> None:
        self.money = money

    def __repr__(self) -> None:
        return f'{self.name} {self.surname}'

    def __del__(self) -> None:
        print(f'???????????????????????? {self.name} {self.surname} ????????????!')

users = []
while True:
    user_main_menu = input('???????????????? ???????? ????????????????: \n1.???????????????? ???????????????????????? \n2.?????????????? ???????????????????????? \n0.??????????\n')
    try:
        user_main_menu = int(user_main_menu)
        if user_main_menu in (0, 1, 2):
            pass
        else:
            print('?????????????? ?????????? ???? 1 ???? 2, ???????? 0 ?????? ????????????!')
    except:
        print('???? ?????????? ???? ??????????!')
        continue
    match user_main_menu:
        case 1:
            user_name = input('?????????????? ??????: ')
            user_surname = input('?????????????? ??????????????: ')
            try:
                user_money = int(input('?????????????? ???????????????????? ??????????: '))
            except:
                print('?????????????? ??????????!')
                user_money = input('?????????????? ???????????????????? ??????????: ')
                while not isinstance(user_money, int):
                    try:
                        user_money = int(user_money)
                    except:
                        print('?????????????? ??????????!')
                        user_money = input('?????????????? ???????????????????? ??????????: ')
            user_currency = input('?????????????? ???????????? (KZT, RUB, USD, EUR): ')
            while user_currency not in ('KZT', 'RUB', 'USD', 'EUR'):
                print('???? ?????????? ?????????????????????? ????????????!')
                user_currency = input('?????????????? ???????????? (KZT, RUB, USD, EUR): ')
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
            print('???????????????????????? ?????????????? ????????????????!\n')
        case 2:
            if len(users) == 0:
                print('?? ?????????? ?????? ??????????????????????????!')
                continue
            for i in range (len(users)):
                print(f'{i + 1}. {users[i]}')
            try:
                user_number = int(input('???????????????? ???????????????????????? ???? ??????????????: '))
            except:
                print('?????????????? ??????????!')
                user_number = input('???????????????? ???????????????????????? ???? ??????????????: ')
                while not isinstance(user_number, int):
                    try:
                        user_number = int(user_number)
                    except:
                        print('?????????????? ??????????!')
                        user_number = input('???????????????? ???????????????????????? ???? ??????????????: ')
            
            account = users[user_number - 1]

            while True:
                print('1 - ???????????? ????????????????')
                print('2 - ?????????????? ????????')
                print('3 - ???????????????????? ????????')
                print('4 - ???????????? ????????????')
                print('5 - ?????????? ????????????')
                print('6 - ?????????????????????? ??????????')
                print('0 - ?????????????? ????????')
                menu = int(input('???????????????? ????????????????: '))
                match menu:
                    case 1:
                        account.toString()
                    case 2:
                        print(account.get_user())
                    case 3:
                        account.set_user(int(input('?????????????? ???????????????????? ??????????: ')))
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
                        print('?????????????? ?????????? ???? 1 ???? 6, ???????? 0 ?????? ???????????? ?? ?????????????? ????????!')
        case 0:
            break
