import threading
from threading import Thread
import requests


def thread_decorator(thread_name, is_daemon):
    def decorator(func):
        def wrapper(urls):
            thread_list = []
            for i, url in enumerate(urls):
                t = Thread(target=func, args=(url,))
                t.name = thread_name + str(i)
                t.daemon = is_daemon
                thread_list.append(t)
                t.start()
            return thread_list

        return wrapper

    return decorator


@thread_decorator(thread_name='Thread_', is_daemon=False)
def get_content(url):
    print(f"{threading.current_thread().name} started\n")
    print(f"get content of {url}\n")
    content = requests.get(url)
    print(f"{threading.current_thread().name} finished\n")


list_url = ['https://github.com/asd894954/python_courses/tree/master/day1',
            'https://github.com/asd894954/python_courses/tree/master/day2',
            'https://github.com/asd894954/python_courses/tree/master/day3',
            'https://github.com/asd894954/python_courses/tree/master/day4',
            'https://github.com/asd894954/python_courses/tree/master/day5',
            'https://github.com/asd894954/python_courses/blob/master/day4/abstract.py',
            'https://github.com/asd894954/python_courses/blob/master/day4/class_work_4.py',
            'https://github.com/asd894954/python_courses/blob/master/day4/comparisson.py',
            'https://github.com/asd894954/python_courses/blob/master/day4/home_work_4.py',
            'https://github.com/asd894954/python_courses/blob/master/day4/meta.py']

thread_list = get_content(list_url)

print(thread_list)



# 1) Создать декоратор, который будет запускать функцию в отдельном потоке. Декоратор должен принимать следующие аргументы: название потока, является ли поток демоном.
# 2) Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор. Создать список из 10 ссылок, по которым будет происходить скачивание. Создать список потоков, отдельный поток, на каждую из ссылок. Каждый поток должен сигнализировать, о том, что, он начал работу и по какой ссылке он работает, так же должен сообщать когда скачивание закончится.
# 3) Написать свой контекстный менеджер для работы с файлами.
# 4) Создать подобие социальной сети. Описать классы, которые должны выполнять соответствующие функции (Предлагаю насследовать класс авторизации от класса регистрации). Добавить проверку на валидность пароля (содержание символов и цифр), проверка на уникальность логина пользователя. Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, потдверждение пароля), далее входит в свою учетную запись. Добавить возможность выхода из учетной записи, и вход в новый аккаунт. Создать класс User, котоырй должен разделять роли обычного пользователя и администратора. При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим, так же пост должен содержать дату публикации. Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.
