
# 1. เขียนโปรแกรมรับค่าตัวเลข 3 จำนวน จากนั้นนำตัวเลขทั้งหมดมาบวกรวมกันและแสดงผลทางจอภาพ
x,y,z = [int(x) for x in input('Ennter 3 values: ').split()]
print(f'summaion is {x+y+z}')


# 2
x = [int(x) for x in input('Enter multi values: ').split()]
print(x,type(x))
print(x+x)