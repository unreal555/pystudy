

# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send():
    sender = '47540479@qq.com'
    receivers = '47540479@qq.com'
    message =  MIMEMultipart('related')
    subject = '刷学习强国啦'
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    message.attach(content)

    file=open("e://5.jpg", "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)



    try:
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(sender,"nqigqkmstuuhcbce")
        server.sendmail(sender,receivers,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
send()