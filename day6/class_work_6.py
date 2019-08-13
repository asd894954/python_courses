class MyList:
    def __init__(self, *args):
        self._list = {}
        for i, item in enumerate(args):
            self._list[i] = item

    def __getitem__(self, item):
        return self._list[item]

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

        tmp_list ={}
        for i, value in enumerate(self._list.values())
            tmp_list[i] = value
        self._list = tmp_list


    def pop(self):
        return self._list.pop(self._list.__len__(), None)

    def index(self, item):
        for key, value in self._list.items():
            if value== item:
                return key
        return None

    def count(self):
        return self._list.__len__()


my_list = MyList(1, 2, 3)

for i in range(3):
    print(my_list[i])

my_list.append(4)

for i in range(4):
    print(my_list[i])
