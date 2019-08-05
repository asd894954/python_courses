my_var = list()
print(type(my_var))

class A:
    pass


B = type("MyNewClass", (), {"Var": "xz"})

print( A )
print(B.__dict__)

b = B()

print(b.__dict__)