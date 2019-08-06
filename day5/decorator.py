from threading import Thread


def decorator(func):
    def wrapper(urls):
        for url in urls:
            t = Thread(target=func, args=(url))
            t.start()

    return wrapper


@decorator
def get_content(*args):
    print(len(args))
    print(args)


list_url = ['link1', 'link2', 'link3']

get_content(list_url)
