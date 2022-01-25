# Copy Dicitonary

x = {1:'Puriwat',2:'Lertkrai',3:'RUTS'}
print(x)
print(x.keys())

# copy ()
y = x
print(y)
y[3] = 'Saiyai'
print(y)
print(x)

y = x.copy()
print(x)
print(y)
y[1] = 'Krerkkeat'
y[2] = 'Dummeee'
print("After changing data in y :")
print(x)
print(y)