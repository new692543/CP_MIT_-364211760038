"""
Name: {เกริกเกียรติ ดำหมี}
SID: {364211760038}
Group: {MIT212}
"""

"""
Question 2:
จงเขียนโปรแกรมจาก tuple ที่กำหนดให้
(10 คะแนน)
"""

myTuple = (100,200,300,400,500)  

# แสดงผลข้อมูลใน myTuple ทั้งหมด
print(myTuple)
# แสดงผลข้อมูล 200 จาก myTuple
print(myTuple[1])
# แสดงผลข้อมูล 500 จาก myTuple
print(myTuple[4])
# แสดงผลข้อมูล 500 จาก myTuple โดยใช้ negative index
print(myTuple[-1])
# แสดงผลข้อมูล (200,300,400) โดยใช้ range index
print(myTuple[1:4])
# แสดงผลข้อมูล (400,500) โดยใช้ range index
print(myTuple[3:])
# แสดงผลข้อมูล (100,200) โดยใช้ range negative index
print(myTuple[:-3])
# แสดงผลข้อมูลใน myTuple ทั้งหมด โดยการใช้ for loop
for x in myTuple:
    print(x, end=' ')
print('\n')

for x in range(len(myTuple)):
    print(myTuple[x])

print('Data in tule with while loop :')
i = 0
while i < len (myTuple):
    print(myTuple[i])
    i+=1

# Tuples ไม่สามารถเพิ่มหรือลบข้อมูลได้ แต่สามารถเปลี่ยน Tuples เป็น List เพื่อเพื่อหรือลบข้อมูล

# เปลี่ยน myTuple เป็น List ชื่อ myList
myList = list(myTuple)
# เพิ่มข้อมูล 10,20,30 ใน myList
myList.append(10)
myList.append(20)
myList.append(30)
# เพิ่มข้อมูล 40 ใน myList ในตำแหน่งที่ 0
myList.insert(0, 40)
# เพิ่มข้อมูล 50 ใน myList ในตำแหน่งที่ 3
myList.insert(3, 50)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูล 10
myList.remove(10)
# ลบข้อมูล 100
myList.remove(100)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# นำข้อมูลใน myList ทั้งหมดบวกรวมกัน และเก็บไว้ในตัวแปร total จากนั้นแสดงตัวแปร total หน้าจอ output

# เปลี่ยน myList เป็น Tuple ในชื่อ myTuple
myTuple = list(myList)
# แสดงผลข้อมูลทั้งหมดใน myTuple
print(myTuple)

