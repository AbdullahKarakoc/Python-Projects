from PyPDF2 import PdfMerger

birlestirici = PdfMerger()

pdf1 = open("pdf1.pdf","rb")
pdf2 = open("pdf2.pdf","rb")




birlestirici.append(pdf1)
birlestirici.append(pdf2)
birlestirici.write("birlesenpdf.pdf")


birlestirici.append(pdf1)
birlestirici.append(2,pdf2)              #eklemek istediğimiz sayfa
birlestirici.write("birlesenpdf2.pdf")
