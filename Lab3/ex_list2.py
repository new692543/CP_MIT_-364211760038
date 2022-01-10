# list comprehension

fruit = ['apple','banana','cheery','pinapple','orange']

# without comprehension
newlist = []
for x in fruit:
    if 'a' in x:
        newlist.append(x)

print('Data in newlist: \n', newlist)

# using comprehension
newlist = [x for x in fruit if 'a' in x]
print('Data in newlist(comprehension):\n',newlist)

num = [23,54,67,34,89,11]
#คัดกรองข้อมูลใน num โดยเลือกเฉพาะข้อมูลที่น้อยกว่า 50
num = [x for x in num if x <50]
print(newlist)
#คัดกรองข้อมูลใน num โดยเลือกเฉพาะข้อมูลที่มากกว่า 30 และน้อยกว่า 90
newlist = [x for x in num if x>30 and x<90]
print(newlist)

#sort data in list
# sort()
# low to high
num.sort()
print(num)
#high to low
num.sort(reverse = True)
print(num)

mylist = ['apple','cherry','banana','mango']
mylist.sort()
print(mylist)
mylist.sort(key = str.lower)
print(mylist)




a,b = 100,200
print(f'a = {a}, b = {b}')