#参数msgfile是msg文件的保存路径
#参数extract_path是提取出的附件的保存路径
import extract_msg,os,shutil
import base64
import re
import set_xlsx_user

def decode_base64_encode_other(coded_str):
    try:
        code = re.findall(r'=\?(.*)\?\w\?.*\?=', coded_str)
        if not code:
            code = re.findall(r'\?(.*)\?\w\?.*\?=', coded_str)
        content = re.findall(r'=\?.*\?\w\?(.*)\?=', coded_str)
        if not content:
            content = re.findall(r'\?.*\?\w\?(.*)\?=', coded_str)
        baseb = base64.b64decode(content[0])
        original_str = str(baseb, encoding=code[0])
    except:
        return coded_str
    return original_str

def extract_msgs(msgfile, extract_path):
    ext_ret = 0
    file_name_list = {}
    msg = extract_msg.Message(msgfile)
    title = msg.subject

    reciver = re.findall(r'<(.*)>', msg.to)
    try:
        if reciver:
            reciver = ','.join(reciver)
        else:
            reciver = decode_base64_encode_other(msg.to)
            reciver = re.findall(r'<(.*)>', reciver)[0]
    except IndexError:
        reciver = msg.to
    try:
        sender = re.findall(r'<(.*)>', msg.sender)[0]
    except:
        sender = msg.sender
    body = msg.body
    body = body.replace('\n', '<br/>')
    msg_attachment = msg.attachments
    if msg_attachment:
        for attachment in msg_attachment:
            attachment.save(customPath=extract_path)
            file_name_list[attachment.longFilename] = attachment.longFilename
        ext_ret = 1
    return ext_ret, file_name_list, title, reciver,sender, body
#ext_ret  邮件中是否有附件
#file_name_list  附件文件名
#title  邮件标题
#reciver  收件人
#sender  发件人
#body  邮件正文内容

source=r'C:\Users\Administrator\Desktop\新建文件夹\source'

for file in os.listdir(source):
    filename, ext = os.path.splitext(file)
    if str.lower(ext) == '.msg':
        print(filename,ext)
        filename=re.sub(' ','',filename)
        dir=os.path.join(source,filename)
        path=os.makedirs(dir)
        print(os.path.join(source,file), dir)

        extract_msgs(msgfile=os.path.join(source,file), extract_path=dir)
        shutil.copy(os.path.join(source,file),dir)
        set_xlsx_user.do(path=dir)