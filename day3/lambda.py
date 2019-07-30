
addition = lambda x,y: x + y

print(addition(1,3))


list_var = [0, 100, -100, 2, 34, -2, -5]

lyam = lambda x: x ** 2
lyam2 = lambda x:  not x % 2

map_var = list( map( lyam , list_var))

print( map_var )

map_var = list( filter( lyam2 , list_var))

print( map_var )