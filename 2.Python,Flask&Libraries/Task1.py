def fun3(z):
    c = z * 4 # 40
    return c

def fun2(y):
    b = fun3(y) * 3 # 120
    return b

def fun1(x):
    a = fun2(x) * 2 #240
    return a 

result = fun1(10)
print(result) #240