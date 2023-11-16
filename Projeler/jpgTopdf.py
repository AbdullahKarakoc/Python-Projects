import sys
import os
import img2pdf

klasör_yolu = "fotolar"
if os.path.isdir(klasör_yolu):
    with open("fotolar.pdf","wb") as pdf_dosya:
        fotolar = []
        for dosya_adi in os.listdir(klasör_yolu):
            if dosya_adi.endswith(".jpg"):
                yol = os.path.join(klasör_yolu,dosya_adi)
                fotolar.append(yol)
        pdf_dosya.write(img2pdf.convert(fotolar))
        
elif os.path.isfile(klasör_yolu):
    if klasör_yolu.endswith(".jpg"):
        with open("fotolar2.pdf","wb") as pdf_dosya:
            pdf_dosya.write(img2pdf.convert(klasör_yolu))

else:
    print("lütfen jpg uzantılı dosya veya klasör giriniz")
    