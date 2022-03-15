"""
Name: {Krerkkreat_Dummee}
SID: {364211760038}
Group: {MIT212}
"""

"""
1.เขียนฟังก์ชันเพื่อบวกเลข 3 ตัว และ return ผลลัพธ์ออกมา ก าหนดให้ฟังก์ชันนี่รับค่า parameter 3 ตัว
คือ a,b,c ที่เป็นจ านวนใดๆ
"""

def getNumber():
    mynumber = []
    for x in range(3):
        mynumber.append(int(input(f'Enter integer [{x+1}]: ')))
    return mynumber
def totalValue(var):
    total = 0
    for x in var:
        total+=x
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The summation of those integer is: {totalValue(mynum)}')



""""
2. เขียนฟังก์ชันเพื่อยกก าลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกก าลังสอง
ออกมา ก าหนดให้ฟังก์ชันนี้รับ parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจ านวนใด ๆ
"""

def getNumber():
    mylist = []
    for x in range(1):
        mylist.append(int(input(f'Enter integer : ')))
    return mylist
def myfunction(var):
    total = 0
    for x in var:
        e = x ** 2
        total = total + e
    return total


mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The result of squaring is: {myfunction(mynum)}')


"""
3. เขียนฟังก์ชัน Calculator(a,b,op) โดยรับ parameter 3 ตัว ได้แก่ a, b ซึ่งเป็นจ านวนใดๆ และ op ซึ่ง
เป็นสายอักขระที่เป็นไปได้ 4 แบบ คือ +, -, *, /
• ถ้า op เป็น + ให้ return a+b
• ถ้า op เป็น - ให้ return a-b
• ถ้า op เป็น * ให้ return a*b
• ถ้า op เป็น / ให้ return a/b
"""

op = ['+', '-', '*', '/']
def calculator():
    a = input('Enter A : ')
    b = input('Enter B : ')
    op = input('Enter OP :')
    if op == '+':
        return 'a+b'
    elif op == '-':
        return 'a-b'
    elif op == '*':
        return 'a*b'
    else:
        return 'a/b'

cal = calculator()
print(cal)


"""
4. เขียนฟังก์ชันเพื่อค่าหาต่ าสุด และค่าสูงสุด ให้ return ผลลัพท์ทั้ง 2 ออกมา ก าหนดให้ฟังก์ชันนี่รับ
parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจ านวนใดๆ
"""
def getNumber():
    listA = []
    for x in range(5):
        listA.append(int(input(f'Enter integer [{x+1}]: ')))
    return listA

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The lowest number is: {min(mynum)}')
print(f'The maximum number is: {max(mynum)}')

"""
5. เขียนโปรแกรมไพธอนเพื่อน าเลขบัตรประชาชนมาบวกันเพื่อท านายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อท านายดวงชะตา ถ้าเป็นเลขคู่ให้ท านายว่า your fortune is
good
• ถ้าเป็นเลขคี่ ให้ท านายว่า your fortune is very good
"""
def getPTD():
    sumPID = [int(x) for x in input(f'Enter PID : ').split()]
    return sumPID

def getFortune(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            resultlist.append('Your fortune is good')
        else:
            resultlist.append('Your fortune is very good')
    return resultlist

PID = getPTD()
print(f'The data from user: {sum(PID)}')
print(f'The prediction result is: {getFortune(sum(PID))}')