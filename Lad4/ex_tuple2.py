# unpacking data in tu

mytuple = (10,20,30)
print(mytuple)

(x,y,z) = mytuple
print(x,y,z)
print(type(x))

mytuple = mytuple * 2
print(mytuple)
(x,y,*z) = mytuple
print(x,y,z)

(x,*y,z) = mytuple
print(x,y,z)


(*x,y,z) = mytuple
print(x,y,z)

# join tuple
x = ('a','b','c')
y = (1,2,3)
z = x+y
print(z)