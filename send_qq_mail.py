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

def send(txt,sender='47540479@qq.com',receiver='47540479@qq.com',subject='python send',img_content=None,img_path=None):
    print('mail----------------------------------------')
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
b64='''data:image/png;base64,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'''
if __name__=='__main__':
    send(txt='ekljflkajsldjfaljflajkljdfal',subject='xuexi',img_content=b64)