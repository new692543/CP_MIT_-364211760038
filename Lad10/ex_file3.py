try:
    # create docx
    f = open('test.docx','x')
except:
    print('Cound not create a docx file.')
else:
    print('docx file is already created.')

    # write text to docxfile
try:
    f = open('test.docx')
    f.write('RUTS')