import requests
import my_html_tools
import json

s=''':authority: m.ctrip.com
:method: POST
:path: /restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031148211154598915
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
content-length: 278
content-type: application/json
cookie: _ga=GA1.2.2052497198.1594255925; _gid=GA1.2.2128817788.1594255925; MKT_OrderClick=ASID=4897155950&AID=4897&CSID=155950&OUID=fpz&CT=1594255925418&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155950%26allianceid%3D4897%26ouid%3Dfpz%26keywordid%3D160662196927%26bd_vid%3D9848696031585510597%26ds_rl%3D1284915%26gclid%3DCKm155L6vuoCFZEOXAodEAsIug%26gclsrc%3Dds&VAL={"pc_vid":"1594255916359.45db8v"}; MKT_Pagesource=PC; MKT_CKID=1594255925687.hcdu0.gouy; MKT_CKID_LMT=1594255925690; _gcl_dc=GCL.1594255926.CKm155L6vuoCFZEOXAodEAsIug; _RF1=58.59.25.123; _RSG=jFKfA5.KxkCm.Xsh7XU3r8; _RDG=28a4fbe634be6029c81d3f9aa6f23dd197; _RGUID=cbbb53e1-4aa5-43ed-8d43-7a11ebda1fb0; Session=SmartLinkCode=U155950&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; nfes_isSupportWebP=1; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&createtime=1594255951&Expires=1594860750882; _bfa=1.1594255916359.45db8v.1.1594255916359.1594257239302.1.5.290510; _bfs=1.3; _bfi=p1%3D10650000804%26p2%3D10650000804%26v1%3D5%26v2%3D3; _jzqco=%7C%7C%7C%7C1594255961816%7C1.474573741.1594255925681.1594255956300.1594257266463.1594255956300.1594257266463.0.0.0.3.3; __zpspc=9.1.1594255925.1594257266.3%232%7Cwww.baidu.com%7C%7C%7C%7C%23
cookieorigin: https://you.ctrip.com
origin: https://you.ctrip.com
referer: https://you.ctrip.com/sight/jinan128/107538.html
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
'''


headers=my_html_tools.tras_header(s)

# 'resourceid'    资源序号，系统指定
# 'resourcetype'    资源类型，系统指定
# 'districtid'      城市的id
# 'districtename'   城市的代码
# 'star'              0全部    5很好   4好  3一般   2差   1很差
# 'tourist'          0不选          1商务旅行     2朋友出游    3情侣出游   4家庭亲子   5单独旅行
# 'order'          3只能排序，2有用数量排序，1时间排序
# 'poiid'
# 'pagenow'    页码
# 'usefulDataId'   是否有用



keys=['resourceid','resourcetype','districtid','districtename','star','tourist','order','poiid','pagenow','usefulDataId']

url='https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031148211154598915'

data={"arg":{"channelType":2,"collapseType":0,"commentTagId":0,"pageIndex":1,"pageSize":50,"poiId":90704,"sourceType":1,"sortType":3,"starType":0},"head":{"cid":"09031148211154598915","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","xsid":"","extension":[]}}

response=requests.post(url,data=json.dumps(data),headers=headers)

str=response.content.decode('utf-8')
print(str)
result=json.loads(str)

count=0
for i in result['result']['items']:
        # print(i)
        userid=i['userInfo']['userId']

        imgs=[]

        for j in i['images']:
                imgs.append(j['imageSrcUrl'])

        if len(i['scores'])==3:
                jingse=i['scores'][0]['score']
                quwei=i['scores'][1]['score']
                xingjiabi=i['scores'][2]['score']
        else:
                jingse=None
                quwei=None
                xingjiabi=None


        content=i['content']

        print(userid,jingse,quwei,xingjiabi,content,imgs,)
        count+=1
print(count)


