
# open file with path
import os

# try:
#     f = open('C:\\Users\Phatchadawadee\Desktop\lab10.txt')
#     print(f.read())
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# delete file
try:
    if os.path.exists('C:\\Users\Phatchadawadee\Desktop\lab10.txt'):
        os.remove('C:\\Users\Phatchadawadee\Desktop\lab10.txt')
    else:
        print('File not found.')
except Exception as e:
    print(e)