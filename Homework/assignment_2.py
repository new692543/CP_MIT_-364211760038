"""
Name: {Krerkkreat_Dummee}
SID: {364211760038}
Group: {MIT212}
"""

myList = [10,20,30,40,50]

# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# แสดงผลข้อมูล 20 จาก myList
print(myList[1])
# แสดงผลข้อมูล 50 จาก myList
print(myList[4])
# แสดงผลข้อมูล 50 จาก myList โดยใช้ negative index
print(myList[-1])
# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[1:4])
# แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[3:5])
# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
print(myList[-5:-3])
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
i = 0
while i < len(myList):
    print(myList[i])
    i += 1
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
for x in range(len(myList)):
    print(myList[x])
# เพิ่มข้อมูล 100,200,300 ใน myList
myList.append(100)
myList.append(200)
myList.append(300)
print(myList)
# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0,400)
print(myList)
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3,500)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# ลบข้อมูล 10
myList.remove(10)
print(myList)
# ลบข้อมูล 100
myList.remove(100)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop(-1)
print(myList)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# เรียงข้อมูล myList จาก น้อย-มาก
myList.sort()
print(f'Sort Low to High: {myList}')
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# เรียงข้อมูล myList จาก มาก-น้อย
myList.sort(reverse=True)
print(f'Sort High to Low: {myList}')
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)

# comprehension
myList = [ 20, 40, 55, 60, 75, 80, 95, 100, ]
print(myList,len(myList))
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
newlist = [x for x in myList if x > 50]
print(newlist)
# แสดงผลข้อมูลใน newList ทั้งหมด
print(newlist)
# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
myFinalist = myList+newlist
print(myFinalist)
# แสดงผลข้อมูลใน myFinalList ทั้งหมด
print(myFinalist)