from abc import ABC, abstractmethod


class BaseCar():

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class car(BaseCar):
    def __init__(self, x):
        delf._x = x



    def set_x(self,x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")
