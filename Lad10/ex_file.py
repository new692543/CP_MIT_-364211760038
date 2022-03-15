# file I/O

# open()
#f = ""


f = open ("demofile.txt",'a') # r - read
print(f.read())
f.write("\nThungsong")
except Exception as e :
    print(e)
else:
    print('File is already updated.')
finally :
    f.close()





