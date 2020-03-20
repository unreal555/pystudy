# -*- coding: utf-8 -*-

# Scrapy settings for demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tujidao'

SPIDER_MODULES = ['tujidao.spiders']
NEWSPIDER_MODULE = 'tujidao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo (+http://www.yourdomain.com)'

import random
# user agent 列表

# USER_AGENT_LIST = [
#     'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
#     'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
#     'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
#     'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
#     'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
#     'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
#     'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
#     'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# ]
# # 随机生成user agent
# USER_AGENT = random.choice(USER_AGENT_LIST)

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


RETRY_ENABLED = True  #打开重试开关
RETRY_TIMES = 8  #重试次数
DOWNLOAD_TIMEOUT = 5  #超时
RETRY_HTTP_CODES = [429,404,403]  #重试

HTTPERROR_ALLOWED_CODES = [301, 302,403,429]     # 返回301, 302时, 按正常返回对待, 可以正常写入cookie



# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.125
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 2
CONCURRENT_REQUESTS_PER_IP = 2

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
# COOKIES_DEBUG=True
# DOWNLOADER_MIDDLEWARES_BASE = {
#     'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
#     'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
#     'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
#     'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
#     'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
#     'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 800,
#     'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
# }

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'demo.middlewares.DemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     'tujidao.middlewares.ProxyMiddleWare':100
   # 'demo.middlewares.DemoDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
REDIRECT_ENABLED = False                  # 关掉重定向, 不会重定向到新的地址

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
     'pipelines.PicPipeline':100,
     # 'pipelines.Normal_File_Pipeline': 200,
     # 'pipelines.Dianzishu_Pipeline':300
}

IMAGES_STORE = 'e:/a' #设置图片下载路径
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
