class MyList:

    def __init__(self, *args):
        self._list = []

        for item in args:
            self._list.append(item)

    def __getitem__(self, item):
        return self._list[item]




list1 = MyList(1,2,3)

print(list1[1])