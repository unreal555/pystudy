#coding=utf-8

import requests
import hashlib
import random
import json
import time

APP_ID='20200227000389406'
key='HuiaSVAxKxmWEhAOIdFx'
salt=str(random.randint(1000000000,9999999999))
f='auto'
t='zh'

def trans(q):
    sign=APP_ID+q+salt+key
    sign=hashlib.md5(sign.encode(encoding='utf-8')).hexdigest()
    while 1:
        req='http://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(q,f,t,APP_ID,salt,sign)
        print(req)
        response=requests.get(req)
        s=response.content.decode('unicode_escape')
        print(s)
        if 'error_code' in s:
            time.sleep(1.5)
            continue
        s=json.loads(s)
        s=s['trans_result'][0]['dst']
        print(s,type(s))
        print('输入{}翻译成{}'.format(q,s))
        return s

print(trans('아비노 시스루 원피스'))


# 通用翻译API接入文档
#
#
#
# 欢迎使用通用翻译API，本文档将指导您如何接入API服务
#
# 如何使用通用翻译API？
#
#     使用您的百度账号登录百度翻译开放平台（http://api.fanyi.baidu.com）；
#     注册成为开发者，获得APPID；
#     进行开发者认证（如仅需标准版可跳过）；
#     开通通用翻译API服务：开通链接
#     参考技术文档和Demo编写代码
#
#
# 接入方式
#
# 通用翻译API通过HTTP接口对外提供多语种互译服务。您只需要通过调用通用翻译API，传入待翻译的内容，并指定要翻译的源语言（支持源语言语种自动检测）和目标语言种类，就可以得到相应的翻译结果。
# 通用翻译API HTTP地址：
#
# http://api.fanyi.baidu.com/api/trans/vip/translate
# 通用翻译API HTTPS地址：
#
# https://fanyi-api.baidu.com/api/trans/vip/translate
#
# 输入参数
#
#
# 请求方式： 可使用GET或POST方式，如使用POST方式，Content-Type请指定为：application/x-www-form-urlencoded
# 字符编码：统一采用UTF-8编码格式
# query长度：为保证翻译质量，请将单次请求长度控制在 6000 bytes以内。（汉字约为2000个）
#
# 签名生成方法
#
# 签名是为了保证调用安全，使用MD5算法生成的一段字符串，生成的签名长度为 32位，签名中的英文字符均为小写格式
# 生成方法：
#
# Step1. 将请求参数中的 APPID(appid)， 翻译query(q, 注意为UTF-8编码), 随机数(salt), 以及平台分配的密钥(可在管理控制台查看) 按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
# Step2. 对字符串1做md5，得到32位小写的sign。
# 注：
# 1. 待翻译文本（q）需为UTF-8编码
# 2.  在生成签名拼接 appid+q+salt+密钥 字符串时，q不需要做URL encode，在生成签名之后，发送HTTP请求之前才需要对要发送的待翻译文本字段q做URL encode
#
# 输出参数
#
# 返回的结果是json格式，包含以下字段：
#
#
# 接入举例
#
# 例如：将英文单词apple翻译成中文：
# 请求参数：
#
#      q=apple
#      from=en
#      to=zh
#      appid=2015063000000001（请替换为您的appid）
#      salt=1435660288（随机码）
#      平台分配的密钥: 12345678
# 生成签名sign：
#
# Step1. 拼接字符串1：
# 拼接appid=2015063000000001+q=apple+salt=1435660288+密钥=12345678得到字符串1：“2015063000000001apple143566028812345678”
# Step2. 计算签名：（对字符串1做md5加密）
# sign=md5(2015063000000001apple143566028812345678)，得到sign=f89f9594663708c1605f3d736d01d2d4
# 拼接完整请求：
#
# http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
# 注：也可使用POST方式，如POST方式传送，Content-Type请指定为：application/x-www-form-urlencoded
#
# 语言列表
#
# 源语言语种不确定时可设置为 auto，目标语言语种不可设置为 auto。但对于非常用语种，语种自动检测可能存在误差。
#
#
# 错误码列表
#
# 当翻译结果无法正常返回时，请参考下表处理：
#
#
# 词典、语音合成资源
#
# 通用翻译API默认不提供词典、语音合成资源。如需使用请先进行企业认证，之后发送邮件至translate_api@baidu.com申请开通词典或语音合成资源，请注明您的使用场景。
# 资源开通后，API翻译结果中将默认附带dict（词典）和tts（语音合成）字段，仅对中英、英中互译有效。
#
# 词典资源：
#
# 词典分中英词典，由于每个词属性不同，词典结果不一定包含所有部分。
# 如源语言为中文，词典数据包括：拼音、词性、中文释义、英文释义、近义词等资源。
# 如源语言为英文，词典数据包括：英文释义、中文释义、音标、核心词汇类别等。
# 注：单个query需为词、词组或短语，如query为句子，则dict字段为空。
# 语音合成资源：
#
# 语音合成资源包含query原文、译文的发音，以mp3文件格式提供。
# 注：单个query内分段数超过3段，或字数超过500字，则tts字段为空。
#
# 自定义术语库
#
# 自定义术语库是百度翻译最新推出的API增值服务，如果您认为通用翻译API对于某些术语翻译不准确，可在“管理控制台-我的术语库”页面填写您认为正确的原文和译文，启用术语库，并在接口URL增加“&action=1”，即可在翻译结果中看到干预效果（提交后需等待10分钟方可生效）。
#
# 需要提醒您的是：因翻译模型并非对术语的一一替换，而是将您填写的术语翻译与原翻译进行对比和计算。如您填写的翻译与原译文差异过大，则可能导致干预后结果有错乱。此外，术语干预仅适用于专有名词、术语的自定义，目前暂不支持针对HTML代码（如<p> <div>）原样输出，即：您暂时无法在原文和译文都填写英文单词“text”。
#
# 各语言DEMO
#
# PHP 版（点击下载）
# JS 版（点击下载）
# Python2 版（点击下载）
# Python3 版（点击下载）
# C 版（点击下载）
# Java 版（点击下载）
# C# 版（点击下载）
#
# 常见问题：
# 1.如何在一次请求中翻译多个单词或者多段文本?
#
# 您可以在发送的字段q中用换行符（在多数编程语言中为转义符号 \n。其中\n是需要能被程序解析出来的换行符而不是字符串\n，您可以将\n用双引号包围 ）或者回车换行来分隔要翻译的多个单词或者多段文本，这样您就能得到多段文本独立的翻译结果了。注意在发送请求之前需对q字段做URL encode！
#
# 2. 什么是URL encode？
#
# 网络标准RFC 1738规定了URL中只能使用英文字母、阿拉伯数字和某些标点符号，不能使用其他文字和符号。如果您需要翻译的文本里面出现了不在该规定范围内的字符（比如中文），需要通过URL encode将需要翻译的文本做URL编码才能发送HTTP请求。大部分编程语言都有现成的URL encode函数，具体使用方法可以针对您使用的编程语言自行搜索。
#
# 3. 通用翻译API中，字符数量如何统计？
#
# 字符数量的统计以翻译的源语言字符长度为标准。一个汉字、一个英文字母、一个标点符号等均记为一个字符
#
# 4. 单次翻译请求是否有字符数限制？
#
# 为保证您的使用体验，请将单次翻译文本长度限定为6000字节以内（汉字约为2000个字符）。此外，高峰时期单次请求文本过长或将导致翻译超时。您可将query分多次请求。
#
# 5. 为什么我的请求总是返回错误码54001？
#
# 54001表示签名错误，请检查您的签名生成方法是否正确。
# 应该对 appid+q+salt+密钥 拼接成的字符串做MD5得到32位小写的sign。确保要翻译的文本q为UTF8格式。
# 注意在生成签名拼接 appid+q+salt+密钥 字符串时，q不需要做URL encode，在生成签名之后，发送HTTP请求之前才需要对要发送的待翻译文本字段q做URL encode。
# 如果您无法确认自己生成签名的结果是否正确，可以将您生成的签名结果和在https://md5jiami.51240.com/中生成的常规md5加密-32位小写签名结果对比。
#
# 6. 为什么我的请求会返回54003？
#
# 54003表示请求频率超限，请降低您的请求频率。
# 对于标准版服务，您的QPS（每秒请求量）=1，如需更大频率，请先进行身份认证，认证通过后可切换为高级版（适用于个人，QPS=10）或尊享版（适用于企业，QPS=100）
# 7. 为什么我的请求会返回58003？
#
# 因黑产采用不正当手段收集用户APPID及密钥，由此产生的盗刷字符量现象日益猖獗，系统风控增加了IP校验规则，如同一IP当日使用多个APPID发送翻译请求，则该IP将被封禁当日请求权限，次日解封。
# 但由于IP多变，应用场景复杂，难免出现误伤正常使用的情况。如您属正常使用，但出现58003的提示，请发送邮件至 translate_api@baidu.com，同时提供如下信息。我方在收到邮件后将与您取得联系，核实后将解除封禁。
# 公司名称：
# 产品名称：
# 联系人：
# 联系方式：
# 服务器IP：
# APPID：
# 注：如提供信息不全，将影响审核通过率。
#
# 8. 如果我需要翻译整个网页，尖括号内的标签无法原样输出，怎么办？
#
# 翻译API会将传入的所有字符串当做可翻译字符，目前暂时无法区分哪些部分需原样保留，因此API不适合直接处理html文件。您可将html文件进行译前处理，抽取出待翻译文本，传入API翻译后再回填。
#
# 9. 是否支持对译文中的术语结果进行修改？
#
# 已认证用户可进入“管理控制台→ 我的术语库”维护术语列表，同时开通“干预通用翻译API结果”。开通后，您将可对译文中的术语翻译结果进行优化和修正。请注意：干预通用翻译API结果将可能导致翻译延时增长。因此在无需干预结果时可将开关关闭。
# 如术语干预功能无法满足您的需要，或有更多意见或建议，可联系translate_api@baidu.com
#
# 10. 我应该如何获取词典、语音合成资源结果？
#
# 接入文档与通用翻译API一致，接入流程上无变化。与未开通词典、语音合成服务相比，仅在返回结果处增加tts、dict字段，请注意辨别字段名称。
# 举例：
# （1）未接入资源时，query=apple，语言方向为英到中，返回结果为：
# {"from":"en","to":"zh","trans_result":[{"src":"apple","dst":"苹果"}]}
# 接入词典、语音合成资源后，返回结果为：
# {"from":"en","to":"zh","trans_result":[{"src":"apple","dst":"苹果","src_tts":"https:\/\/fanyiapp.cdn.bcebos.com\/api\/tts\/95e906875b87d342d7325a36a4e1ab42.mp3","dst_tts":"https:\/\/fanyiapp.cdn.bcebos.com\/api\/tts\/62f4ff87617655bc1f65e24cf4ed4963.mp3","dict":"{"lang":"1","word_result":{"simple_means":{"word_name":"apple","from":"original","word_means":["苹果"],"exchange":{"word_pl":["apples"]},"tags":{"core":["高考","考研"],"other":[""]},"symbols":[{"ph_en":"ˈæpl","ph_am":"ˈæpl","parts":[{"part":"n.","means":["苹果"]}],"ph_other":""}]}}}"}]}
# （2）未接入资源时，query=中国，语言方向为中到英，返回结果为：
# {"from":"zh","to":"en","trans_result":[{"src":"中国","dst":"China"}]}
# 接入词典、语音合成资源后，返回结果为：
# {"from":"zh","to":"en","trans_result":[{"src":"中国","dst":"China","src_tts":"https:\/\/fanyiapp.cdn.bcebos.com\/api\/tts\/d943b8e0e31e8d0ea8879dde5d41f016.mp3","dst_tts":"https:\/\/fanyiapp.cdn.bcebos.com\/api\/tts\/2e2312a1d33e2ff453f92d5d95277e13.mp3","dict":"{"lang":"0","word_result":{"simple_means":{"symbols":[{"word_symbol":"zhōng guó","parts":[{"part_name":"","means":[{"text":"China","part":"n.","word_mean":"China","means":["中国"]},{"text":"Sino-","part":"comb.","word_mean":"Sino-","means":["中国的","中国人(的)"]}]}]}],"word_name":"中国","from":"CEDict","word_means":["China","Sino-"]}}}"}]}
#
# 11. 我已开通词典、语音合成资源，但不想在结果中呈现，应该怎么办？
#
# 如需隐藏词典、语音合成信息，可在拼接请求参数时附加"&dict=1&tts=1"，例如，如仅需隐藏tts字段，完整请求为：
# http://api.fanyi.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4&tts=1
#
# 12. 我怎样开通“我的术语库”功能？
#
# “我的术语库”功能面向个人及企业认证用户开放，您需首先前往“开发者信息”处完成身份认证，认证后即可在管理控制台看到“我的术语库”入口。目前自定义术语功能已开通“中文”和“英语”两个语种，更多语种需求，请发送邮件至translate_api@baidu.com告诉我们。
#
# 13. 为什么我添加了术语却看不出效果？
#
# 添加术语却看不出效果，可能出于以下几个原因：
# a. 添加或修改术语后，需要大约10分钟的生效时间，如果您是刚刚修改过术语，请您耐心等候生效；
# b. 翻译系统判断您定义的翻译与原翻译差异过大。由于神经网络翻译模型中，术语的定制化干预功能并非对翻译结果的生硬替换，而是类似于“调优”。如果您对术语的定义与原释义含义差距过大，会导致经计算过后的出现不可控的翻译结果。如您对术语干预效果不满意，请与我们联系。translate_api@baidu.com
#
