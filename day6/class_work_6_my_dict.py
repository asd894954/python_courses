class MyDict:

    def __init__(self):
        self._keys = []
        self._values = []

    def __setitem__(self, key, value):
        if key in self._keys:
            self._values[self._keys.index(key)] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __getitem__(self, item):
        if isinstance(item, int):
            try:
                return self._keys[item]
            except KeyError:
                raise IndexError
        else:
            if item in self._keys:
                return self._values[self._keys.index(item)]
            else:
                return None

    def get(self, key):
        if key in self._keys:
            return self._values[self._keys.index(key)]
        else:
            return None

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        result = []
        for i in range(self._keys.__len__()):
            result.append((self._keys[i], self._values[i]))
        return result

    def __add__(self, other):
        result = MyDict()
        
        for key, value in self.items():
            result[key] = value

        for key, value in other.items():
            result[key] = value

        return result


my_dict = MyDict()

my_dict['asd'] = 23
my_dict['asd1'] = 2222

print(my_dict['asd'])
print(my_dict.get('asd'))

for i in my_dict:
    print(i)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

d1 = MyDict()
d1['asd'] = 22
d1['asd2'] = 23

d2 = MyDict()
d2['asd'] = 44
d2['asd3'] = 55

d3 = d1 + d2
print(d3.items())
