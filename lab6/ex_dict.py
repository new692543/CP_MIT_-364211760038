# Dictionary --> key:value

mydict = {'brand':'totoya',
          'model': 'Altis',
          'year': 2021}
print(mydict)
print(f'type of mydict: {type(mydict)}')
print(f'Length of mydict: {len(mydict)}')

#access to data in dictionary
# key
print(mydict['brand']) # toyota
print(mydict['model']) #
print(mydict['year']) #

# keys ()
x = mydict.keys()
print(x,type(x))
#values()
x = mydict.values()
print(x, type(x))
#loop
for x in mydict:
    print(x) # --> keys
for x in mydict:
    print(mydict[x]) # --> values
#loop uing keys(), values() , items()
for x in mydict.keys():
    print(x) #---> key
for x in mydict.values():
    print(x) #----> vaiues
for x,y in mydict.items():
    print(f'key: {x} value: {y}')

# get()
print(mydict.get('brand'))

# change data in dictionary
# key
mydict['model'] = 'Fortuner'
print(mydict)

# update()
mydict.update({'year':2022})
print(mydict)

# check key
if 'Brand' in mydict:
    print(mydict['Brand']) # --> value
else:
    print('This key does not exist.')

# Add data to dictionay
# key
mydict['color'] = ['black','white']
print(mydict)
# updata()
mydict.update({'price':150000})
print(mydict)
mydict.update({'color':['Red']})
print(mydict)
print(mydict['color'][0])
mydict['color'].append('White')
print(mydict)

# remove data in dictionary
print(mydict.keys())
# pop ()
mydict.pop('color')# remove key : 'color'
print(mydict)
# popitem () --> remove last data
mydict.popitem()
print(mydict)
# del
del mydict['year']
print(mydict)
#del  mydict # delete completely
#print(mydict)

# clear data in dicitonary
# clear ()
mydict.clear()
print(mydict)
