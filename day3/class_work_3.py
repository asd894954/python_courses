class Point():

    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z


    _x = None

    def set_x(self,x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

    _y = None

    def set_y(self,y):
        self._y = y

    def get_y(self):
        return self._y

    def del_y(self):
        del self._y

    y = property(get_y, set_y, del_y, "I'm the 'y' property.")

    _z = None

    def set_z(self,z):
        self._z = z

    def get_z(self):
        return self._z

    def del_z(self):
        del self._z

    z = property(get_z, set_z, del_z, "I'm the 'z' property.")



    def __add__(self, other):

        return Point(self._x + other._x, self._y + other._y, self._z + other._z )

    def __sub__(self, other):
        return Point( self._x - other._x, self._y - other._y, self._z - other._z)

    def __mul__(self, other):
        return Point(self._x * other._x, self._y * other._y, self._z * other._z)

    def __floordiv__(self, other):
        return Point(self._x / other._x, self._y / other._y, self._z / other._z)

    def __neg__(self):
        return Point(-self._x , -self._y , -self._z)


    def print(self):
        print( "x = {}, y = {}, z = {} ".format(self._x, self._y,self._z))

    def __str__(self):
        return "x = {}, y = {}, z = {} ".format(self._x, self._y, self._z)




p1 = Point(1, 2, 3)
p2 = Point(1, 2 ,3)

p3 =  p1 + p2
p3.print()

p1.x = 3

p3 =  p1 + p2
print( p3 )
