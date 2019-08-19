import re
import shelve


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.errors = message


class Storage:
    def __init__(self, file_name='storage.db'):
        self._file_name = file_name

    def set(self,key, value):
        with shelve.open(self._file_name)as db:
            db[key]= value

    def get(self, key, value=None):
        with shelve.open(self._file_name)as db:
            result = db.get(key,value)
        return result



class Registaration:

    def regTest(self,password,pattern, message):

        p = re.compile(pattern)

        if not p.match( password ):
            raise CustomException(f"Password:\"{password}\" must contain {message}")

    def doRegister(self,login, password, password_confirmation):
        if  password != password_confirmation:
            raise CustomException("Password not equal")

        self.regTest(password, r'.{8,}','at least 8 character')
        self.regTest(password,r".*\d", 'digit')
        self.regTest(password,'.*[a-z]', 'lowercase later')
        self.regTest(password,'.*[A-Z]', 'Uppercase later')
        self.regTest(password,'.*[^\w\s]', 'Special character')

        st = Storage()

        users = st.get('users',[])

        if login in users:
            raise  CustomException('User alredy registered')



reg =  Registaration()

try:
    reg.doRegister('asd','aads','asds')
except CustomException as error:
    print(error)


try:
    reg.doRegister('asd','asd','asd')
except CustomException as error:
    print(error)


try:
    reg.doRegister('asd','asdasdasd','asdasdasd')
except CustomException as error:
    print(error)


try:
    reg.doRegister('asd','asdasdasd1','asdasdasd1')
except CustomException as error:
    print(error)


try:
    reg.doRegister('asd','ASDASDASD1','ASDASDASD1')
except CustomException as error:
    print(error)

try:
    reg.doRegister('asd','asdASDASDASD1','asdASDASDASD1')
except CustomException as error:
    print(error)

try:
    reg.doRegister('asd','~asdASDASDASD1','~asdASDASDASD1')
except CustomException as error:
    print(error)

class User:

    def __init__(self):
        self.logout()




    def _isAdmin(foo):
        def decorator(self, *args,**kwargs):
            if not self._admin:
                raise CustomException("You are not admin")
            else:
                foo(self,  *args,**kwargs)
        return decorator

    def _isLogged(foo):
        def decorator(self, *args,**kwargs):
            if not self._logged:
                raise CustomException("You are not logged")
            else:
                foo(self, *args,**kwargs)
        return decorator

    def logout(self):
        self._logged = None
        self._admin = None
        self._login =None

    def _notLogged(foo):
        def decorator(self, *args, **kwargs):
            if self._logged:
                self.logout()
                print('You are forced to logout')
            foo(self, *args, **kwargs)
        return decorator

    @_notLogged
    def register(self, login, password, password_confirmation):
        reg = Registaration()
        reg.doRegister(login,password, password_confirmation)

    @_isLogged
    def list_post(self):
        pass

    @_isLogged
    @_isAdmin
    def list_all_post(self):
        pass

    @_isLogged
    def add_post(self,post):
        pass


    @_isLogged
    @_isAdmin
    def hello(self):
        print("hello")


user = User()

try:
    user.hello()
except CustomException as error:
    print(error)