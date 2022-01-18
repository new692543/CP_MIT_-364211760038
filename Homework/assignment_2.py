"""
Name: {Krerkkreat_Dummee}
SID: {364211760038}
Group: {MIT212}
"""

mylist = []
print(mylist)
print(type(mylist))


myList = ['10','20','30','40','50']
print(myList)     # แสดงผลข้อมูลใน myList ทั้งหมด

print(myList[1])  # แสดงผลข้อมูล 20 จาก myList
print(myList[4])  # แสดงผลข้อมูล 50 จาก myList
print(myList[-1]) # แสดงผลข้อมูล 50 จาก myList โดยใช้ negative index


myList = ['10','20','30','40','50']
print(len(myList))

print(myList[1:4])    # แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[2:])    # แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[3:])    # แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[:2])    # แสดงผลข้อมูล {10,20} โดยใช้ range negative index


print('Display with for loop:')
for x in mylist:
    print(x, type(x))
# while
print('Display with for loop:')
i =0
while i < (len(mylist)):
    print(mylist[i], type(mylist[i]))
    i+=1



# เพิ่มข้อมูล 100,200,300 ใน myList
myList = [100,200,300]
print(myList)

print(myList)
myList[0] = 1000
print(myList)
myList[-1] = 3000
print(myList)
#add data into list

# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
# แสดงผลข้อมูลใน myList ทั้งหมด

# ลบข้อมูล 10
# ลบข้อมูล 100
# แสดงผลข้อมูลใน myList ทั้งหมด
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
# แสดงผลข้อมูลใน myList ทั้งหมด

# เรียงข้อมูล myList จาก น้อย-มาก
# แสดงผลข้อมูลใน myList ทั้งหมด


# เรียงข้อมูล myList จาก มาก-น้อย
# แสดงผลข้อมูลใน myList ทั้งหมด

# comprehension
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
# แสดงผลข้อมูลใน newList ทั้งหมด

# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
# แสดงผลข้อมูลใน myFinalList ทั้งหมด