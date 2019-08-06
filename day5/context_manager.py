# https://stackoverflow.com/questions/35483359/handling-exceptions-inside-context-managers


class File:
    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode

    def __enter__(self):
        self._file = open(self._file_name, self._mode)
        return self._file

    def __exit__(self, *args):
        self._file.close()
        print(args)
        return True


with File('asd.txt', 'w') as f:
    f.write('asd\nasd\nasd')
    print(1 / 0)
