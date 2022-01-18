# join set

x = {10,20,30,40,50}
y = {11,22,33,44,55,10,20}
print(f'x = {x} y = {y}')


# union() --->
z = x.union(y)
print(z)


# update()
x.update(y)
print(x)

# set intersection
a = {10,20,30,40,50}
b = {40,20,60,70,80}
# intersection() --> new set
c = a.intersection(b)
print(c)
# intersection_update()
a.intersection_update(b)
print(a)

# symmrtric_differece() --> newset
# a = {40,20}
c = a.symmetric_difference(b)
print(c)

# symmrtric_differece_update()
a.symmetric_difference_update(b)
print(a)

print(f' a = {a}')
print(f' b = {b}')
# issubset()
print(a.issubset(b))
print(b.issubset(a))
# issuperset()
print(a.issuperset(b))
print(b.issuperset(a))
