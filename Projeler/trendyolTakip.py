import requests
from bs4 import BeautifulSoup
from sendEmailTY import sendMail
import time

url="https://www.trendyol.com/delpino/baharlik-erkek-mevsimlik-ceket-p-687250273?advertItems=https://www.trendyol.com/jaglion/erkek-yeni-sezon-deri-ceket-p-51741355="


def checkPrice(url,paramPrice):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    page = requests.get(url,headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')


    productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

    price = htmlPage.find("span",class_="prc-org").getText()

    image = htmlPage.find("img",class_="base-product-image")

    convertedPrice = float(price.replace(",",".").replace("TL",""))


    if(convertedPrice <= paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent="""\
            
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle,image,url)
            
        sendMail("abdullahkrkc1453@gmail.com","Ürünün fiyatı düştü",htmlEmailContent)
    else:
        print("ürün fiyatı düşmedi")  

    print(convertedPrice)
    
while(True):
    checkPrice(url,550)
    time.sleep(3)