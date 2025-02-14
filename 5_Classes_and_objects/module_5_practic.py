class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    '''
    Класс пользователя, содержащий атрибуты: лагин, пароль
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choise = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choise == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль!')
            else:
                print('Пользователь не найден')
        if choise == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password2 := input('Повторите пароль: '))
            if password != password2:
                print('Пароли не совпадают')
                continue
            database.add_user(user.username, user.password)
        print(database.data)

# Атрибуты - это переменные внутри класса
# Методы - это функции внутри класса
# Переменные которые создаются на основе этого класса называются экземплярами либо же объектами этого класса