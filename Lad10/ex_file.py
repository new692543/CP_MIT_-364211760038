
# File I/O

# open()
"""
r - read
a - append - create and write at the end of file
w - write - overwrite content
x - create file with empty content
"""
try:
    f = open("demofile.txt",'a')
    f.write("\nPhatchadawadee")
except Exception as e:
    print(e)
else:
    print('File is already updated.')
finally:
    f.close()


