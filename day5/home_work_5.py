import re
import shelve


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

        users = st.get('users', [])

        if login in users:
            raise CustomException('User alredy registered')


class User:

    def __init__(self):
        self.logout()

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

    @except_decorator
    @_is_logged
    def list_post(self):
        pass

    @except_decorator
    @_is_logged
    @_is_admin
    def list_all_post(self):
        pass

    @except_decorator
    @_is_logged
    def add_post(self, post):
        pass

    @except_decorator
    @_is_logged
    @_is_admin
    def hello(self):
        print("hello")


user = User()

user.hello() 

user.register('asd', 'aads', 'asds')
user.register('asd', 'asd', 'asd')
user.register('asd', 'asdasdasd', 'asdasdasd')
user.register('asd', 'asdasdasd1', 'asdasdasd1')
user.register('asd', 'ASDASDASD1', 'ASDASDASD1')
user.register('asd', 'asdASDASDASD1', 'asdASDASDASD1')
user.register('asd', '~asdASDASDASD1', '~asdASDASDASD1')
