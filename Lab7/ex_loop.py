# while and for loop

"""
พิมพ์ HELLov5 ครั้ง
"""
# while
print('Hello from while loop:')
i = 1
while i <=5:
    print('Hello')
    i+=1

# for
print('Hello from for loop:')
for x in range(5): # 0 1 2 3 4
    print('hello')

mylist = ['toyota','mazda','honda','nissan','mg','gwm']
# for
for x in mylist:
    print(x,type (x))
# whaile
i = 0
while i < len(mylist):
    print(mylist[i], type(mylist[i]))
    i+=1