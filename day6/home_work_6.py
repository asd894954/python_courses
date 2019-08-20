import re
import shelve
from datetime import datetime


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.errors = message


class Storage:
    def __init__(self, file_name='storage.db'):
        self._file_name = file_name

    def set(self, key, value):
        with shelve.open(self._file_name)as db:
            db[key] = value

    def get(self, key, value=None):
        with shelve.open(self._file_name)as db:
            result = db.get(key, value)
        return result

    def get_keys(self):

        with shelve.open(self._file_name)as db:
            result = list(db.keys())
        return result


class Registaration:

    @staticmethod
    def reg_test(password, pattern, message):

        p = re.compile(pattern)

        if not p.match(password):
            raise CustomException(f"Password:\"{password}\" must contain {message}")

    def do_register(self, login, password, password_confirmation):
        if password != password_confirmation:
            raise CustomException("Password not equal")

        self.reg_test(password, r'.{8,}', 'at least 8 character')
        self.reg_test(password, r".*\d", 'digit')
        self.reg_test(password, '.*[a-z]', 'lowercase later')
        self.reg_test(password, '.*[A-Z]', 'Uppercase later')
        self.reg_test(password, '.*[^\w\s]', 'Special character')

        st = Storage()

        userexist = st.get(login, None)

        if userexist:
            raise CustomException('User alredy registered')

        user = dict([('login', login),
                     ('password', password),
                     ('isadmin', False),
                     ('reg_date', datetime.now()),
                     ('post', [])])
        st.set(login, user)


class User:

    def __init__(self):
        self._logged = None
        self._admin = None
        self._login = None
        self._post = []

    def make_me_admin(self):
        self._admin = True

    def _is_admin(func):
        def decorator(self, *args, **kwargs):
            if not self._admin:
                raise CustomException("You are not admin")
            else:
                func(self, *args, **kwargs)

        return decorator

    def _is_logged(func):
        def decorator(self, *args, **kwargs):
            if not self._logged:
                raise CustomException("You are not logged")
            else:
                func(self, *args, **kwargs)

        return decorator

    def except_decorator(func):
        def decorator(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except CustomException as error:
                print(error)

        return decorator

    def logout(self):
        self._logged = None
        self._admin = None
        self._login = None
        self._post = []

    def _not_logged(func):
        def decorator(self, *args, **kwargs):
            if self._logged:
                self.logout()
                print('You are forced to logout')
            func(self, *args, **kwargs)

        return decorator

    @_not_logged
    @except_decorator
    def register(self, login, password, password_confirmation):
        reg = Registaration()
        reg.do_register(login, password, password_confirmation)

    @_not_logged
    @except_decorator
    def login(self, login, password):
        st = Storage()

        user = st.get(login, None)

        if not user:
            raise CustomException("wrong login or password")

        if password != user['password']:
            raise CustomException("wrong login or password")

        self._logged = True
        self._login = login
        self._admin = user['isadmin']
        self._post = user['post']

    @except_decorator
    @_is_admin
    def list_users(self):
        st = Storage()

        users = st.get_keys()
        print(users)

    @except_decorator
    @_is_logged
    def list_post(self):
        for date, post in self._post:
            print(date.strftime("%Y-%B-%d %X"), post)

    @except_decorator
    @_is_logged
    @_is_admin
    def list_post_for_user(self, user_login):
        st = Storage()
        user = st.get(user_login, {})

        if user != {}:
            for date, post in user.get('post'):
                print(date.strftime("%Y-%B-%d %X"), post)

    @except_decorator
    @_is_logged
    def add_post(self, post):
        st = Storage()

        user = st.get(self._login)
        self._post.append((datetime.now(), post))
        user['post'] = self._post
        st.set(self._login, user)


user = User()

user_register_login = 'asd2'

user.register(user_register_login, 'aads', 'asds')
user.register(user_register_login, 'asd', 'asd')
user.register(user_register_login, 'asdasdasd', 'asdasdasd')
user.register(user_register_login, 'asdasdasd1', 'asdasdasd1')
user.register(user_register_login, 'ASDASDASD1', 'ASDASDASD1')
user.register(user_register_login, 'asdASDASDASD1', 'asdASDASDASD1')

user.register(user_register_login, '~asdASDASDASD1', '~asdASDASDASD1')

user.login('asd', 'asd')
user.login(user_register_login, 'asd')
user.login(user_register_login, '~asdASDASDASD1')

user.add_post('Первый твит')

user.list_post()

user.list_post_for_user('asd')
user.list_users()

user.make_me_admin()
user.list_users()
user.list_post_for_user('asd2')


# 4) Создать подобие социальной сети. Описать классы, которые должны выполнять
# соответствующие функции (Предлагаю насследовать класс авторизации от класса регистрации).
# Добавить проверку на валидность пароля (содержание символов и цифр),
# проверка на уникальность логина пользователя. Человек заходит, и имеет возможность
# зарегистрироваться (ввод логин, пароль, потдверждение пароля), далее входит в свою
# учетную запись. Добавить возможность выхода из учетной записи, и вход в новый аккаунт.
# Создать класс User, котоырй должен разделять роли обычного пользователя и администратора.
# При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим,
# так же пост должен содержать дату публикации. Под учётной записью администратора мы можем
# увидеть всех пользователей нашей системы, дату их регистрации, и их посты.
