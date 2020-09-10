
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import base64
import re

smtp_server="smtp.qq.com"
smtp_port=465
smtp_keys="nqigqkmstuuhcbce"

def send(txt,sender='47540479@qq.com',receiver='47540479@qq.com',subject='python send',img_content=None):

    if not isinstance(txt,str):
        print('文件内容为文本类型，请重新输入')
        return 0

    print('send mail from {} to {},subject {}'.format(sender,receiver,subject))

    message =  MIMEMultipart('related')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    if img_content==None:
        print('无图邮件')
        content= MIMEText('{}'.format(txt), 'html', 'utf-8')
        message.attach(content)
    else:
        print('有图邮件')
        content = MIMEText('<html><body>{}</br><img src="cid:imageid" alt="imageid"></body></html>'.format(txt), 'html', 'utf-8')
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
                    print('有文件头',data)
                    img_data = base64.b64decode(data)
                else:
                    print('无文件头',img_content)
                    img_data=base64.b16decode(img_content)

            if isinstance(img_content,bytes):
                    img_data=img_content

        img = MIMEImage(img_data)
        print(img)
        img.add_header('Content-ID', 'imageid')
        message.attach(img)

    try:

        server=smtplib.SMTP_SSL(smtp_server,smtp_port)
        server.login(sender,smtp_keys)
        server.sendmail(sender,receiver,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except Exception as e:
        print(e)

if __name__=='__main__':
    send('屋里',subject='xuexi')