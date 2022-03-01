#function

print('start')

def myfuncA():
    print('Hello A')

def myfuncB(x):
    print('Hello B',x)

def myfuncC(x,y):
    print('Hello c',(x+y))

def myfuncD(*x):  # --> tuple
    print(x)
    total = 0
    for i in x :
        print(i, end=" ")
        total += i
    # return total valun
    return  total

def myfuncE(x,y,z):
    print(f'x={x} y={y} z={z}')
    print(f'summation of value is: {x+y+z}')

def myfuncF(**num): #num --> dictionary
    for x in num.items():
        print(x)
    t = 0
    for x in num.values():
        t += x
    print(f'total value from myfuncF: {t}')

# default parameter
def myfuncG('country = thailand'):
    print('country')


#calling function

myfuncA()
myfuncB(100)
myfuncC(100,200)
print('total value : ',myfuncD(100,200,300,400,500))
re = myfuncD(100,200,300,400,500)
print(re)
#keyword arigeument
myfuncE(z=100,x=200,y=300)
myfuncF(num1=100,num2=200,num3=300)
# default parameter
myfuncG(
    myfuncG('maylasia')






print('\nEnd')
