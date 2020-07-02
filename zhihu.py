#!/bin/py
#   -*-coding:utf-8-*-
import re, my_html_tools, requests
import json

headers = '''
authority: www.zhihu.com
method: GET
path: /question/54689409/answer/1226800079
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: _zap=d4acdaa0-5f8f-4ac7-a1d5-ec7f61dc2bac; _xsrf=M9KKd8LZC6dCja1boAC32JeTRi5UPoAc; d_c0="AJDZg7eaPBGPTjTFpmQwRKmHzPryqSOT9-k=|1588904866"; capsion_ticket="2|1:0|10:1590477955|14:capsion_ticket|44:NzcwMGE5MTY0YzcwNGY1MjllNjM5Y2JmZDBhYzg3MWM=|f3ba99b2203f523dc8f26ccb66bd64c6ea83e2c97d583aa96a293ea48c6927c9"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1588908749,1589167113,1590461314,1590477953; SESSIONID=OrngvNTcx7SEyfN8MsyVBFEWGi4BR1XJ9yQVpWmUgTr; JOID=V1gXB0kqrpP5sEfqWCvsCj8FTbxOYN77mMEMvD1VnMK6zyahYotuX6ayQO5Y62xuv53lD15XhcfrR6Pl7xORWlU=; osd=UFgVBE4trpH6t0DqWijrDT8HTrtJYNz4n8YMvj5Sm8K4zCGmYoltWKGyQu1f7GxsvJriD1xUgsDrRaDi6BOTWVI=; z_c0="2|1:0|10:1590478048|4:z_c0|92:Mi4xN2ZBRkd3QUFBQUFBa05tRHQ1bzhFU1lBQUFCZ0FsVk40Qks2WHdCcmtPaUlvM1RQNlRRMEV4aXNEdnRDSFRKTzR3|d7301ecaa859cbb5a681d2de3bf468f987f2006e60c296fbc6857c7d9af88673"; unlock_ticket="AKCYo88YOBEmAAAAYAJVTejLzF77_SpxuTGj1A2RxMRU8FFrlOkYJg=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590479230; KLBRSID=76ae5fb4fba0f519d97e594f1cef9fab|1590479233|1590477949
pragma: no-cache
referer: https://www.zhihu.com/
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
'''

headers = my_html_tools.tras_header(headers)

url = 'https://www.zhihu.com/api/v4/questions/54689409/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=20&offset=20&platform=desktop&sort_by=default'
response = requests.get(url, headers=headers)
s = json.loads(response.text)

for i in s['data']:
    i['content'] = i['content'].replace('<br/>', '\r\n')

    print(i['id'])
    print(my_html_tools.qu_html_lable(i['content']))
    print('\r\n')

    with open('./zhihu.txt', 'a', encoding='utf-8') as f:
        f.write(str(i['id']) + '\r\n')
        f.write(my_html_toolsqu_html_lable(i['content']) + '\r\n')
        f.write('#' * 100 + '\r\n')
