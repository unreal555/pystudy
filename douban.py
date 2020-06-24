import requests
import re
import json


def parse_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url, headers=headers)
    text = response.text

    regix = '<div class="pic">.*?<em class="">(.*?)</em>.*?<img.*?src="(.*?)" class="">.*?div class="info.*?class="hd".*?class="title">(.*?)</span>.*?class="other">' \
            '(.*?)</span>.*?<div class="bd">.*?<p class="">(.*?)<br>(.*?)</p>.*?class="star.*?<span class="(.*?)"></span>.*?' \
            'span class="rating_num".*?average">(.*?)</span>'

    results = re.findall(regix, text, re.S)
    for item in results:
        down_image(item[1], headers=headers)
        yield {
            '电影名称': item[2] + ' ' + re.sub('&nbsp;', '', item[3]),
            '导演和演员': re.sub('&nbsp;', '', item[4].strip()),
            '评分': star_transfor(item[6].strip()) + '/' + item[7] + '分',
            '排名': item[0]
        }


def main():
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
        for item in parse_html(url):
            print(item)
            write_movies_file(item)


def write_movies_file(str):
    with open('douban_film.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(str, ensure_ascii=False) + '\n')


def down_image(url, headers):
    r = requests.get(url, headers=headers)
    filename = re.search('/public/(.*?)$', url, re.S).group(1)
    with open(filename, 'wb') as f:
        f.write(r.content)


def star_transfor(str):
    if str == 'rating5-t':
        return '五星'
    elif str == 'rating45-t':
        return '四星半'
    elif str == 'rating4-t':
        return '四星'
    elif str == 'rating35-t':
        return '三星半'
    elif str == 'rating3-t':
        return '三星'
    elif str == 'rating25-t':
        return '两星半'
    elif str == 'rating2-t':
        return '两星'
    elif str == 'rating15-t':
        return '一星半'
    elif str == 'rating1-t':
        return '一星'
    else:
        return '无星'


if __name__ == '__main__':
    main()