# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
import re
import os
import requests

smtp_server="smtp.qq.com"
smtp_port=465
smtp_keys="nqigqkmstuuhcbce"

def send_qq_mail(txt,sender='47540479@qq.com',receiver='47540479@qq.com',subject='python send',img_content=None,img_path=None):

    message =  MIMEMultipart('related')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    if img_content==None and img_path==None:
        print('wutu')
        content= MIMEText('{}'.format(txt), 'html', 'utf-8')
        message.attach(content)
    else:
        print('youtu')
        content = MIMEText('<html><body>{}<img src="cid:imageid" alt="imageid"></body></html>'.format(txt), 'html', 'utf-8')
        message.attach(content)
        if img_content!=None :
            if isinstance(img_content,str):
                if 'data:image' in img_content:
                    print('base64 图片，转码中。。。。')
                    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", img_content, re.DOTALL)
                    if result:
                        ext = result.groupdict().get("ext")
                        data = result.groupdict().get("data")
                    else:
                        raise Exception("Do not parse!")
                    img_data = base64.b64decode(data)

            if isinstance(img_content,bytes):
                    img_data=img_content

        if img_path!=None:
            if os.path.exists(img_path):
                with open(img_path, "rb") as f:
                    img_data = f.read()


        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'imageid')
        message.attach(img)
    try:
        server=smtplib.SMTP_SSL(smtp_server,smtp_port)
        server.login(sender,smtp_keys)
        server.sendmail(sender,receiver,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)

requests('')
if __name__=='__main__':
    send_qq_mail(txt='ekljflkajsldjfaljflajkljdfal',subject='xuexi')