class Stack:
    def __init__(self, *args):
        self._stack = []
        for item in args:
            self._stack.append(item)

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop(len(self._stack) - 1)

    def __str__(self):
        ret = ""
        for item in self._stack:
            if ret == "":
                ret = repr(item)
            else:
                ret = "{}, {}".format(ret, repr(item))
        return ret


print("Stack here")
a = Stack(1, 2, 3)
a.push(4)

print(a)

b = a.pop()
print(b)
print(a)


class Queue:
    def __init__(self, *args):
        self._queue = []

        for item in args:
            self._queue.append(item)

    def push(self, item):
        self._queue.append(item)

    def get_first(self):
        return self._queue.pop(0)

    def count(self):
        return len(self._queue)

    def __str__(self):
        ret = ""
        for item in self._queue:
            if ret == "":
                ret = repr(item)
            else:
                ret = "{}, {}".format(ret, repr(item))
        return ret


print("Queue here")
q = Queue(1, 2, '3')
print(q)
q.push(4)
print(q)

tmp = q.get_first()

print(tmp)
print(q)


class ComplexNumber:
    def __init__(self, r, i):
        self._i = i
        self._r = r

    def set_i(self, i):
        self._i = i

    def get_i(self):
        return self._i

    def del_i(self):
        del self._i

    i = property(get_i, set_i, del_i, "I'm the 'i' property.")

    def set_r(self, r):
        self._r = r

    def get_r(self):
        return self._r

    def del_r(self):
        del self._r

    r = property(get_r, set_r, del_r, "I'm the 'r' property.")

    def __add__(self, other):
        return ComplexNumber(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return ComplexNumber(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        i = self.i * other.r + self.r * other.i

        r = self.r * other.r - self.i * other.i

        return ComplexNumber(r, i)

    def __truediv__(self, other):
        augmented = ComplexNumber(other.r, - other.i)

        dividen = self * augmented

        tmp_var = other.r ** 2 + other.i ** 2

        return ComplexNumber(dividen.r / tmp_var, dividen.i / tmp_var)

    def __str__(self):
        return "({}, {}i)".format(self.r, self.i)


print("Complex numbers")
a = ComplexNumber(3, -1)
b = ComplexNumber(2, -2)

print(a)
print(b)

print('a+b')
print(a + b)
print('a-b')
print(a - b)
print('a*b')
print(a * b)
print('a/b')
print(a / b)
