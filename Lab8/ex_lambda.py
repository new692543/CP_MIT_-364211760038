# lambda function

x = lambda  a: a*a
x = lambda  a,b,c: a+b+c

def myfunc(num):
    print(num)
    return lambda x: x+num





print(x(10,20,30))
x = myfunc(10)
print(x(10))