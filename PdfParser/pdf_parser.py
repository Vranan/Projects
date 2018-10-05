from PyPDF2 import PdfFileReader
f = open('Napolean.pdf','rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText()
f.close()
print(contents)
