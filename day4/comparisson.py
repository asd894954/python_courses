import datetime
import requests



def decorator(func):

    def wrapper0():



        a = datetime.datetime.now()
        func(  )
        b = datetime.datetime.now()

        print(b - a)


    return wrapper0

@decorator
def get_url1():

    asd = []
    for i in range(9000):
        asd.append( i )

@decorator
def get_url2():
    asd = [x for x in range(9000)]


get_url1()
get_url2()
