from threading import Thread
import random
import time


def random_generator(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 5))
        print(f"i'm executing from{thread_name}")
    print(f"end of thread {thread_name}")


thread1 = Thread(target=random_generator, args=(5, 'Thread1'))
thread2 = Thread(target=random_generator, args=(5, 'Thread2'))


# thread1.start()
# thread2.start()


def file_writer(file_name, num_of_lines):
    with open(file_name, "w") as f:
        for l in range(num_of_lines):
            f.write(str(random.randint(0, 5000)) + "\n")


list_of_thread = []

for i in range(10):
    t = Thread(target=file_writer, args=(f"./tmp_files/file{i}.txt", random.randint(0, 100)))

    list_of_thread.append(t)
    t.start()

print(list_of_thread)


class RandomGeneratorThread(Thread):
    def __init__(self, num, name):
        self._num = num
        self._name = name
        Thread.__init__(self, name=self._name)

    def run(self):
        for i in range(self._num):
            time.sleep(random.randint(0, 5))
            print(f"i'm executing from{self._name}")
        print(f"end of thread {self._name}")


a = RandomGeneratorThread(5, 'Thread a')
b = RandomGeneratorThread(5, 'Thread b')
a.daemon = True
b.daemon = True
a.start()
b.start()
