# Operators

# Assign operator - สัญลักษณ์ที่ใช้กำหนดตัวแปร
x = 100
print(x)
x += 100  # x= x+100 --> x = 100+100
print(x)
x -= 50  # x -50 --> x = 200-50
print(x)
x **= 2  # x = x*x  = x = 150*150
print(x, type(x))

# matmatic opperator
x, y = 100, 200
print('x is ', x, '\n y is', y)
print('sum of x and y is ', x + y)
print('sum of x and y is ', x - y)
z = x - y
print(z, type(z))
print('multiply of and y is ', x * y)
print('divide of x and y is ', x / y)  # 100/200 = 0.5
print('modulus of x and y is', x % y)
print('floor division fo x and y ', x // y)  # int
z = x // y
print(z, type(z))

# comparaion operators --> True, False
x = 10
y = 20
print(x == y)  # Flase
print(x != y)  # True
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

# Logical operators --> and,or,not
x, y = 10, 20
# and
print(x > 5 and y > 5)  # True
# or
print(x > 5 or y > 5)  # True
# not
z = True
print(z)
print(not z)

# bitwise operators
x = 10
y = 5
# &
print(x & y)  # 0000 1010 & 0000 0101
print(x | y)  # 0000 1110
# ^
print(x ^ y)
# ~
print(~x)
# shaift right -- >>
print(x << 3)
print(x >> 3)

# identity operators --> is , is not
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(x is y)  # False
print(x is not y)  # True
z = x
print(z is x)
print(x[0])
print(z[0])
z[0] = 100
print(x[0])
print(z[0])

a = 10
b = 10
print(a is b)
print(a is not b)
