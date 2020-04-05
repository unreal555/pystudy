import  scrapy

agent={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '125',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'oa.sdnz.xyz:808',
    'Origin': 'http://oa.sdnz.xyz:808',
    # 'Referer': 'http://oa.sdnz.xyz:808',
    # 'Upgrade-Insecure-Requests': '1'
     }

formdata={
    'UNAME':'zl',
    'PASSWORD': '7895123'
}
class Myoa888_Spider(scrapy.Spider):
    name = 'myoa888'
    allowed_domains = 'sdnz.xyz'

    def start_requests(self):
        yield scrapy.FormRequest('http://oa.sdnz.xyz:808/logincheck.php', formdata=formdata,headers=header, callback=self.parse)

    def parse(self,response):
        print(response.text)
        print(response.headers.getlist('Set_Cookie'))
        print(response.url)
        yield scrapy.Request('http://oa.sdnz.xyz:808/general/email/inbox/?BOX_ID=0', headers=header,
                                 callback=self.tparse,dont_filter=True)
    def tparse(self,response):
        print('start scrapy')
        print(response.text)