# tuple

mytuple = ('apple','banana','cherry','papaya','orang')
print(type(mytuple))

#access item in tuple
#index
print(mytuple[0]) #apple
print(mytuple[4]) #orange
#negative index
print(mytuple[-1]) #orange
print(mytuple[-3]) #cherry
# range index
print(mytuple[2:4]) #index 2-3 --> list
print(mytuple[:3]) #index 0-2
print(mytuple[2:]) #index 2-End
#range negative index
print(mytuple[-4:-2])
print(mytuple[-4:])

#loop
#for
for x in mytuple:
    print(x, end=' ')
print('\n')

#for with index
for x in range(len(mytuple)):
    print(mytuple[x])
#while
print('Data in tule with while loop :')
i = 0
while i < len (mytuple):
    print(mytuple[i])
    i+=1

# update data in tuple
# tranform tuple to list
mylist = list(mytuple)
print(mylist)
print(type(mylist))
mytuple[-1] = 'mango'
print(mylist)

mytuple = 'mango'
print(mylist)

mytuple = 'mango'
print(mylist)




#list --> tuple
mytuple = tuple(mylist)
print(mytuple)

# del
 del mytuple
#print(mytuple)







