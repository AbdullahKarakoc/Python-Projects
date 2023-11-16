import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail,subject,content):
    fromMail = "mrx00101101@gmail.com"
    server = smtplib.SMTP("smtp.google.com",587)
    
    server.starttls()
    
    server.login(fromMail,"*145366123.")
    
    message = MIMEMultipart('alternative')
    message['Subject']= subject
    
    
    htmlContent = MIMEText(content,'html')
    message.attach(htmlContent)
    
    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    print("Eposta gönderildi")
    
    server.quit