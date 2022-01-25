# nested dictionary

car1 = {'brand':'TOyota','model':'Altis','price':800000}
car2 = {'brand':'Honda','model':'Civic','color':'blue'}
car3 = {'brand':'Mazda','model':'Mazda 3'}

mycar = {'car1': car1,
         'car2': car2,
         'car3': car3}

print(mycar.get('car1'))
print(mycar.get('car2'))
print(mycar.get('car3'))

print(mycar['car1']['brand']) # Toyota

for x in mycar['car1']:
    print(x)
for x in mycar['car1']:
    print(mycar['car1'][x])