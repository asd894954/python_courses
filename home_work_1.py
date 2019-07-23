asd = []
for i in range(101):
    if not i % 2:
        asd.append(i)

print(asd)

asd = [1,2,3,10]
if 10 in asd:
    print("aga")

aDict = {}
for i in range(5):
    str = 'strana{}'.format(i)
    aDict[str] = 'capital{}'.format(i)


print(aDict)

aDict["strana1"] = "столица1"
aDict["strana2"] = "столица2"
aDict["strana3"] = "столица3"
aDict["strana4"] = "столица4"
aDict["strana5"] = "столица5"

print(aDict)


asd=[]

for key in aDict:
    asd.append(key)

print(asd)


for xz in asd:
    print(aDict.get(xz))

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print( a, b )

def xz( x, y):
    return (x , y)

a , b = xz( 1 , 32)

print( a , b)
def add(*args):
    return(sum(args))

