# -*- coding: utf-8 -*-
#巨坑 request.meta['proxy']一定要用小写，首字母也不能用大写，不然代理不生效。。。坑爹
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64
from scrapy import signals
import random




class ProxyMiddleWare(object):
    USER_AGENT_LIST = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ]

    # 随机选出代理信息
    proxy_list = [
        {'proxy_ip':None},
        {'proxy_ip':"58.59.25.122:1234",'auth':base64.b64encode(bytes("test:594188", 'utf-8'))},
        {'proxy_ip':"58.59.25.123:1234",'auth':base64.b64encode(bytes("test:594188", 'utf-8'))}
    ]

    # request.headers['Proxy-Authorization'] = b'Basic ' + auth

    # 设置代理ip (http/https)

    # if ((request.url).split('//'))[0]=='http':
    #     request.meta['Proxy']='http://{}'.format(proxy)
    # if ((request.url).split('//'))[0]=='https:':
    #     request.meta['Proxy']= 'https://{}'.format(proxy)


    def process_request(self, request, spider):

        proxy=random.choice(self.proxy_list)
        if proxy['proxy_ip']==None:  # No Proxy
            pass
        if proxy['proxy_ip']!=None:         #Use Proxy
            # print('Use proxy:{}'.format(proxy['proxy_ip']),((request.url).split('://'))[0],((request.url).split('://'))[0]=='http',)
            if ((request.url).split('://'))[0]=='http':
                print('http')
                request.meta['proxy']='http://{}'.format(proxy['proxy_ip'])   #巨坑 request.meta['proxy']一定要用小写，首字母也不能用大写，不然代理不生效。。。坑爹
            if ((request.url).split('://'))[0]=='https':
                print('https')
                request.meta['proxy']= 'https://{}'.format(proxy['proxy_ip'])  #巨坑 request.meta['proxy']一定要用小写，首字母也不能用大写，不然代理不生效。。。坑爹
        if 'auth' in proxy.keys():
            request.headers['Proxy-Authorization'] = b'Basic ' + proxy['auth']


        if 'hywly.com'in request.url:
            # request.headers[':authority']='img.hywly.com',
            # request.headers[':method']='GET',
            # request.headers[':scheme']='https',
            # request.headers[':path']=request.url.split('com')[1]
            # request.headers['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            # request.headers[ 'User-Agent'] = random.choice(self.USER_AGENT_LIST),
            # request.headers[ 'accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
            # request.headers[ 'accept-encoding'] = 'gzip, deflate, br'
            # request.headers[ 'accept-language'] = ' zh-CN,zh;q=0.9'
            # request.headers[ 'cache-control'] = ' no-cache'
            # request.headers[ 'pragma'] = ' no-cache'
            # request.headers[ 'sec-fetch-dest'] = ' document'
            # request.headers[ 'sec-fetch-mode'] = ' navigate'
            # request.headers[ 'sec-fetch-site'] = ' none'
            # request.headers[ 'sec-fetch-user'] = ' ?1'
            # request.headers[ 'upgrade-insecure-requests'] = '1'
            # request.headers[ 'Referrer Policy'] = ' no-referrer-when-downgrade'
            # request.headers['Referer'] = request.url,
            # request.headers['if-modified-since']='if-modified-since:Tue, 06 Jun 2017 11:59:14 GMT'
            request.headers['host'] = request.url.split('/')[2],
            request.headers['DNT'] = '1',
            request.headers['Accept'] = 'text/html, application/xhtml+xml, */*',
            request.headers['Accept-Language'] = 'zh-CN'
            request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
            request.headers['Accept-Encoding'] = 'gzip, deflate'
            request.headers['Connection'] = 'Keep-Alive'
            request.headers['Cache-Control'] = 'no-cache'

        if 'action=save' in request.url:
            request.headers[':authority'] = 'www.tujidao.com',
            request.headers[':method'] = 'POST',
            request.headers[':path'] = '?action=save',
            request.headers['accept'] = 'application/json, text/javascript, */*; q=0.01',
            request.headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8',
            request.headers['origin'] = 'https://www.tujidao.com',
            request.headers['x-requested-with'] = 'XMLHttpRequest',
            request.headers['referer'] = 'https://www.tujidao.com/?action=login',
            # request.headers[''] = '',



        else:
            # request.headers['authority']='www.tujidao.com'
            # request.headers['Accept']= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # request.headers[ 'Accept-Encoding']= 'gzip, deflate,br',
            # request.headers['method'] = 'get',
            # request.headers['scheme'] = 'https',
            # request.headers['upgrade-insecure-requests'] = '1',
            # request.headers[ 'Accept-LangPHPSEuage']= 'zh-CN,zh;q=0.9',
            # request.headers[ 'Cache-Control']= 'no-cache',
            # request.headers['Referer']= 'http://www.tujidao.com/u/?action=login',
            # request.headers['Origin'] ='http://www.tujidao.com',
            # request.headers['cookie'] = '''
            # PHPSESSID=vbme8jcjlifncfni3h0r2iiog4; UM_distinctid=174959e7ca5633-02359b14e2d56b-46440d2a-140000-174959e7cf12de; CNZZDATA1257039673=1250971660-1600234379-https%253A%252F%252Fwww.tujidao.com%252F%7C1600238352
            # '''

            request.headers[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        print('request url   :',request.url)
        print('request header:',request.headers)

class DemoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DemoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
