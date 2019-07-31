import datetime
import requests



def decorator( func  ):

    def wrapper0( url ):

        def wrapper1(   count ):

            for i in range(count):
                a = datetime.datetime.now()
                func( url )
                b = datetime.datetime.now()

                print(b - a)

        return wrapper1
    return wrapper0

@decorator
def get_url(url):
    f = requests.get(url)


get_url("https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python")(5)


