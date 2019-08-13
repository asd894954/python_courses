class MyList:
    def __init__(self, *args):
        self._list = {}
        for i, item in enumerate(args):
            self._list[i] = item

    def __getitem__(self, item):
        try:
            return self._list[item]
        except KeyError:
            raise IndexError

    def __setitem__(self, key, value):
        if key > self._list.__len__():
            raise Exception("Index out of range")

        self._list[key] = value

    def append(self, item):
        self._list[self._list.__len__()] = item

    def clear(self):
        self._list.clear()

    def insert(self, idx, item):
        if idx > self._list.__len__():
            raise Exception("Index out of range")
        self._list[idx] = item

    def remove(self, idx):
        if idx > self._list.__len__():
            raise Exception("Index out of range")
        self._list.pop(idx, None)

        tmp_list = {}
        for i, value in enumerate(self._list.values()):
            tmp_list[i] = value
        self._list = tmp_list

    def pop(self):
        return self._list.pop(self._list.__len__() - 1, None)

    def index(self, item):
        for key, value in self._list.items():
            if value == item:
                return key
        return None

    def count(self):
        return self._list.__len__()

    def __add__(self, other):
        ret = MyList()

        for i in self._list.values():
            ret.append(i)

        for i in other._list.values():
            ret.append(i)
        return ret

    def __str__(self):
        ret = ''

        for i in self._list.values():
            if ret == '':
                ret = repr(i)
            else:
                ret = ret + ', ' + repr(i)
        return ret


a = MyList(1, 2, 3)
b = MyList(4, 5, 6)

print(a[0])
a[0] = 8
print(a)

a.append(9)
print(a)
print(a.count())
a.clear()

print(a)

a = MyList(9, 8, 7)

c = a + b
print(c)

c.remove(0)
print(c)
