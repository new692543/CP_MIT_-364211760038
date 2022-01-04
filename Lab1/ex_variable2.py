# Global variable

x = 'MIT'
print(x)


def myfunc():
    # local variable
    x = 'RUTS'
    print(x)


def myfunc2():
    global x
    x = 'Satya'
    print(x)

# call myfunc()
myfunc2()
print(x)
