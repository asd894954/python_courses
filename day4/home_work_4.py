from abc import abstractmethod
import datetime


class Person:
    def __init__(self, name, faculty, birthday):
        self._name = name
        self._faculty = faculty
        self._birthday = birthday

    def set_birthday(self, birthday):
        self._birthday = birthday

    def get_birthday(self):
        return self._birthday

    def del_birthday(self):
        del self._birthday

    birthday = property(get_birthday,
                        set_birthday,
                        del_birthday,
                        "I'm the 'birthday' property.")

    def set_faculty(self, faculty):
        self._faculty = faculty

    def get_faculty(self):
        return self._faculty

    def del_faculty(self):
        del self._faculty

    faculty = property(get_faculty,
                       set_faculty,
                       del_faculty,
                       "I'm the 'faculty' property.")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def del_name(self):
        del self._name

    name = property(get_name,
                    set_name,
                    del_name,
                    "I'm the 'name' property.")

    @abstractmethod
    def get_info(self):
        pass

    def get_age(self):
        today = datetime.date.today()

        if today.month < self.birthday.month or \
                (today.month == self.birthday.month and
                         today.day < self.birthday.day):
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year


class Enrollee(Person):
    def __init__(self, name, faculty, birthday):
        super().__init__(name, faculty, birthday)

    def get_info(self):
        return f"Имя: {self.name}\nДата рождения: {self.birthday}" + \
               f"\nФакультет: {self.faculty}\n"


class Student(Person):
    def __init__(self, name, faculty, birthday, course):
        super().__init__(name, faculty, birthday)
        self._course = course

    def set_course(self, course):
        self._course = course

    def get_course(self):
        return self._course

    def del_course(self):
        del self._course

    course = property(get_course,
                      set_course,
                      del_course,
                      "I'm the 'course' property.")

    def get_info(self):
        return f"Имя: {self.name}\nДата рождения: {self.birthday}" + \
               f"\nФакультет: {self.faculty}" + \
               f"\nКурс: {self.course}\n"


class Teacher(Person):
    def __init__(self, name, faculty, birthday, position, expirience):
        super().__init__(name, faculty, birthday)
        self._position = position
        self._expirience = expirience

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def del_position(self):
        del self._position

    position = property(get_position,
                        set_position,
                        del_position,
                        "I'm the 'position' property.")

    def set_expirience(self, expirience):
        self._expirience = expirience

    def get_expirience(self):
        return self._expirience

    def del_expirience(self):
        del self._expirience

    expirience = property(get_expirience,
                          set_expirience,
                          del_expirience,
                          "I'm the 'expirience' property.")

    def get_info(self):
        return f"Имя: {self.name}\nДата рождения: {self.birthday}" + \
               f"\nФакультет: {self.faculty}" + \
               f"\nПозиция: {self.position}" + \
               f"\nОпыт: {self.expirience}\n"


persons = [Student('name1', 'Python', datetime.date(1980, 1, 1), 4),
           Student('name2', 'Math', datetime.date(1980, 1, 20), 3),
           Enrollee('name3', 'Python', datetime.date(1980, 1, 20)),
           Enrollee('name4', 'English', datetime.date(1979, 5, 20)),
           Teacher('Teacher 1', 'Slizerin', datetime.date(1945, 6, 22), 'Archmag', 40),
           Teacher('Teacher 2', 'Slizerin', datetime.date(1945, 5, 22), 'Archmag', 41)]

for person in persons:
    print(person.get_info())
    # print( person.get_age())

print("\nFiltered")
persons2 = [person for person in persons if person.get_age() == 39]

for person in persons2:
    print(person.get_info())
