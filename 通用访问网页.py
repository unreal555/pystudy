#***conding=utf-8****#

'''
知乎的大坑，'accept-encoding':'gzip, deflate ,br',一定要去掉br,否则乱码
'''

import json
import re
import requests
import mytools

s='''
    cache-control: private, must-revalidate, no-store
    content-encoding: br
    content-type: text/html; charset=utf-8
    date: Wed, 03 Jun 2020 03:32:23 GMT
    pragma: no-cache
    server: CLOUD ELB 1.0.0
    set-cookie: tst=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT; httponly
    set-cookie: KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1591155143|1591155084; Path=/
    status: 200
    strict-transport-security: max-age=15552000; includeSubDomains
    surrogate-control: no-store
    vary: Accept-Encoding
    x-backend-response: 0.509
    x-cdn-provider: tencent
    x-content-type-options: nosniff
    x-daa-tunnel: hop_count=1
    x-edge-timing: 0.539
    x-frame-options: SAMEORIGIN
    x-idc-id: 2
    x-lb-timing: 0.521
    x-nws-log-uuid: 0823fabd-1bec-4956-9909-8caac2003a8d
    x-secng-response: 0.51999998092651
    x-udid: AJAaV47hWxGPTnuC0zeBvC_UMsSpB4hLczE=
    x-via: DIANXIN-SHANDONG_40(200:miss)
    x-xss-protection: 1; mode=block
    :authority: www.zhihu.com
    :method: GET
    :path: /
    :scheme: https
    accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    accept-encoding: gzip, deflate
    accept-language: zh-CN,zh;q=0.9
    cache-control: max-age=0
    cookie: _zap=4b27045c-2467-4056-b639-4e5d59de8b21; d_c0="AJAaV47hWxGPTnuC0zeBvC_UMsSpB4hLczE=|1591003810"; _ga=GA1.2.1506570305.1591003811; _gid=GA1.2.1666575742.1591147888; _xsrf=YeRqeviyEvDfonvqidF5McTxg62Wv8Ni; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1591003811,1591147888,1591155085; _gat_gtag_UA_149949619_1=1; SESSIONID=QcJW6GpSRllN9reRuLvliRlBxexmGX58lYRLQURIenv; JOID=VlgdA0groj6snEGJFC9BKAEzZ9QJfsl8-K0C8U9-ylrqpjToTrW74vafTYkf2aHdqQyQDaM0ekkrz2NwcBA73OM=; osd=W1sVAkomoTatnkyKHC5DJQI7ZtYEfcF9-qAB-U58x1nipzblTb264PucRYgd1KLVqA6dDqs1eEQox2JyfRMz3eE=; capsion_ticket="2|1:0|10:1591155104|14:capsion_ticket|44:M2FjNGYzNGRhZmE1NGE3M2FhMzI2MGJjNmJhNjE1MDQ=|7b4147b328333684f5271085e18a9a403c94feb8b85785a0096de984a9affc21"; z_c0="2|1:0|10:1591155130|4:z_c0|92:Mi4xN2ZBRkd3QUFBQUFBa0JwWGp1RmJFU1lBQUFCZ0FsVk51bWZFWHdEcDd5TlVzWllxSzhZYnVfSzI0Ujd2bjZlMDd3|53e8a609975176f2ad30b1ca3ac653b173b9230a8a856d1d79bec61530720c6c"; unlock_ticket="AKCYo88YOBEmAAAAYAJVTcIg115b47KfHQqaZRyN8bk7TI5CC1FBZQ=="; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1591155130; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1591155134|1591155084
    referer: https://www.zhihu.com/signin?next=%2F
    sec-fetch-dest: document
    sec-fetch-mode: navigate
    sec-fetch-site: same-origin
    sec-fetch-user: ?1
    upgrade-insecure-requests: 1
    user-agent: Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
'''
url='https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=a09fe43ed401d4ed951fcc60974d4a1d&desktop=true&page_number=1&limit=10&action=down&after_id=1&ad_interval=-1'
domain=''

def get_headers(s):
    headers=mytools.tras_header(s)
    return headers

def get_page(url,headers=get_headers(s)):
    return requests.get(url,headers=headers)


response=get_page(url)

s = json.loads(response.text)

for i in s['data']:
    print(i)
    break
