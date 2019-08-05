from abc import ABC, abstractmethod

class Persona( ):

    def __init__(self, fio, fakultet, birthday):
        self._fio = fio
        self._fakultet = fakultet
        self._birthday = birthday

    def set_birthday(self, birthday):
        self._birthday = birthday

    def get_birthday(self):
        return self._birthday

    def del_birthday(self):
        del self._birthday

    birthday = property(get_birthday, set_birthday, del_birthday, "I'm the 'birthday' property.")

    def set_fakultet(self, fakultet):
        self._fakultet = fakultet

    def get_fakultet(self):
        return self._fakultet

    def del_fakultet(self):
        del self._fakultet

    fakultet = property(get_fakultet, set_fakultet, del_fakultet, "I'm the 'fakultet' property.")

    def set_fio(self, fio):
        self._fio = fio

    def get_fio(self):
        return self._fio

    def del_fio(self):
        del self._fio

    fio = property(get_fio, set_fio, del_fio, "I'm the 'fio' property.")

    @abstractmethod
    def info(self):
        pass


    @abstractmethod
    def get_age(self):
        pass



class Abiturient(Persona):

    def info(self):
        print( self.fio, self.birthday, self.fakultet )



class Student(Persona):

    def __init__(self, fio, fakultet, birthday, kurs):
        super().__init__(fio, fakultet, birthday )
        self._kurs = kurs


    def set_kurs(self,kurs):
        self._kurs = kurs

    def get_kurs(self):
        return self._kurs

    def del_kurs(self):
        del self._kurs

    kurs = property(get_kurs, set_kurs, del_kurs, "I'm the 'kurs' property.")


    def info(self):
        print( self.fio, self.birthday, self.fakultet, self.kurs)


    def get_age(self):
        pass



class Teacher(Persona):




    def __init__(self, fio, fakultet, birthday, position, expirience):
        super().__init__(  fio, fakultet, birthday )
        self._position = position
        self._expirience = expirience

    def set_position(self,position):
        self._position = position

    def get_position(self):
        return self._position

    def del_position(self):
        del self._position

    position = property(get_position, set_position, del_position, "I'm the 'position' property.")




    def set_expirience(self,expirience):
        self._expirience = expirience

    def get_expirience(self):
        return self._expirience

    def del_expirience(self):
        del self._expirience

    expirience = property(get_expirience, set_expirience, del_expirience, "I'm the 'expirience' property.")



    def info(self):
        print( self.fio, self.birthday, self.fakultet, self.position, self.expirience )

    def get_age(self):
        pass





students = []

students.append( Student('fio1', 'Python', 123, 4 ))

students[0].info()


