"""
Name: {เกริกเกียรติ ดำหมี}
SID: {364211760038}
Group: {MIT212}
"""

"""
Question 1:
จงเขียนโปรแกรมจากจากคำสั่งต่อไปนี้
(10 คะแนน)
"""

# ประกาศตัวแปร x มีค่าเท่ากับ 100
x = 100
# แสดงผลค่าตัวแปร x
print(x)
# แสดงชนิดข้อมูลของตัวแปร x 
print(type(x))
# ประกาศตัวแปร  y มีค่าเท่ากับ 200
y = 200
# แสดงผลค่าตัวแปร y
print(y)
# แสดงชนิดข้อมูลของตัวแปร y 
print(type(y))
# แสดงผลค่าตัวแปร x และ y โดยมีข้อความดังนี้  "x is 100 and y is 200"
print('x is ',x,'and y is ',y,'')

# ประกาศตัวแปร z มีค่าเท่ากับ ตัวแปร x ลบด้วยตัวแปร y
z = x-y
# แสดงผลค่าตัวแปร z โดยมีข้อความดังนี้  "z is {z}" โดยการใช้ formatted print  -- > print(f{...})
print(f'z = {z}')
# หาผลรวมของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x+y+z
# แสดงผลค่าตัวแปร total โดยการใช้ formatted print  -- > print(f{...})
print(f'total = {total}')
# หาผลลบของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x-y-z
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'total = {total}')
# หาผลคูณของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x*y*z
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'total = {total}')
# หาผลหารของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x%y%z
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'total = {total}')
# หาผลหารแบบจำนวนเต็ม (floor division) ของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x/y/z
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'total = {total}')
