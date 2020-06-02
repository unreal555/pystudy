import requests
import mytools
import re
import os

proxies = {
    "http": "http://test:594188@58.59.25.122:1234",
    }

domain='http://www.ting89.com'

url='http://www.ting89.com/books/15314.html'

@mytools.execute_lasts_time
def get_book(url):
    response=requests.get(url)
    page=mytools.qu_kong_ge(response.content.decode('gbk'))
    bookname=re.findall('<title>(.*?)</title>',page)[0]

    print(bookname)

    done=''
    if os.path.exists('./log.txt'):
        with open('./log.txt','r',encoding='utf-8') as f:
            done=f.read()

    if os.path.exists('./wrong.txt'):
        with open('./wrong.txt','r',encoding='utf-8') as f:
            done=done+f.read()

    if bookname in done:
        return 0


    if os.path.exists(bookname):
        pass
    else:
        os.makedirs(bookname)

    all=re.findall('''<li><ahref='(.*?)'target="_blank">(.*?)</a></li>''',page)
    print(all)

    for i in all:
        try:
            print(domain+i[0])
            chapter=domain+i[0]
            response=requests.get(chapter,proxies=proxies)
            page=response.content.decode('gbk')
            page=mytools.qu_kong_ge(page)
            down=re.findall(r'''下载保存时请自行重命名</div><iframesrc="http://play.ting89.com/down/down.php\?url=(.*?)"height''',page)[0]

            with open('./{}/{}'.format(bookname,'list.txt'),'a',encoding='utf-8') as f:
                f.write('\t'+down+'\r\n')
            mytools.random_wait(1,2)

        except:
            with open('./wrong.txt','a',encoding='utf-8'):
                f.write(bookname+'######'+url+'\r\n')
            break




    with open('./log.txt','a',encoding='utf-8') as f:
        f.write(bookname+'######'+url+'\r\n')


get_book('http://www.ting89.com/books/15314.html')


# response=requests.get(down)
# with open('./{}/{}'.format(bookname,down.split('/')[-1]),'wb') as f:
#     f.write(response.content)