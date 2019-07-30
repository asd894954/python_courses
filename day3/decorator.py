import datetime
import requests



def decorator( func ):

    def wrapper( url ):


        for i in range(10):
            a = datetime.datetime.now()
            func( url )
            b = datetime.datetime.now()

            print(b - a)

    return wrapper 

@decorator
def get_url(url):
    f = requests.get(url)


get_url("https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python")



