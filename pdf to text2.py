import PyPDF2
newfile=open("hello.txt",'w')
file=open('sample.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageobj=pdfreader.getPage(0)
newfile.write(pageobj.extractText())
file.close()
newfile.close()

