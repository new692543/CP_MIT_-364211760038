


try:
    # create docx
    f = open('test.docx','x')
except:
    print('Cound not create a docx file.')
else:
    print('docx file is already created.')

# write text to docxfile
try:
    f = open('test.docx','a')
    f.write('RUTS')
except:
    print('Can not write text to docx file.')
else:
    print('docx file is updated.')
finally:
    f.close()

# read text from docx file
try:
    f = open('test.docx')
    print(f.read())
except:
    print('can not read text from docx file.')
finally:
    f.close()