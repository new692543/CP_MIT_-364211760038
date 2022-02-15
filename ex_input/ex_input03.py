# Input mltiple values

# x,y = input('Enter 2 values: ').split()
# print(x,type(x))
# print(y,type(y))

# list comprehension
#x,y,z = [int(x) for x in input('Ennter 3 values: ').split()]
#print(x,type(x))
#print(y,type(y))
#print(z,type(z))

# input multi integer
# x = [int(x) for x in input('Ennter muti values: ').split()]
# print(x,type(x))

# input multi values
x = [int(x) for x in input('Ennter muti values: ').split()]
print(x,type(x))

# input multi values seperated by ","
x = [x for x in input('Enter multi values (seperated by ","):').split(",")]
print(x,type(x))