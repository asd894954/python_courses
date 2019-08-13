list = [1, 2, 3]

b = iter(list)


class NumberGenerator():
    def __init__(self, start,end):
        self._start = start
        self._end = end

    def __next__(self):
        ret = end


class MyArray:
    __slots__ = "_size", "_type", "_array"
    def __init__(self, size, vartype):
        self._size = size
        self._type = vartype

        self._array = [0] * size

    def __getitem__(self, idx):
        if idx > self._size - 1:
            raise Exception("Out of range")

        return self._array[idx]


arr = MyArray(10,1)

print(arr[0])