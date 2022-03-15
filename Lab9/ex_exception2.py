# Input Exception

#try:
# num = int(input('Enter an integer:'))
# print(f'The number that you entered is : {num}')
#except Exception as e:
 #   print(e)

num = input('Enter an integer: ') # str
 if not type(num) is int: # num is not integer
     raise  TypeError('ONLY INTEGER ARE ALLOWED.')

 try:
     something_went_wrong()
except Exception as e :
    print(e.args)
print(f'The number that you entered is : {num}')

