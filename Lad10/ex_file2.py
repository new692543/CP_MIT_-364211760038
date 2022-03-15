# open file with path


try:
    f = open('C:\\Users\USER\Desktop\New Text Document.txt')
    print(f.read())
except Exception as e :
    print(e)
finally:
    f.close()