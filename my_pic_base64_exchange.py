
import base64
import re
import uuid
'''
png to base64
base64 to png
'''

def base64_to_pic(src):
    """
    解码图片
    :param src: 图片编码
        eg:
            src="data:image/gif;base64,R0lGODlhMwAxAIAAAAAAAP///
                yH5BAAAAAAALAAAAAAzADEAAAK8jI+pBr0PowytzotTtbm/DTqQ6C3hGX
                ElcraA9jIr66ozVpM3nseUvYP1UEHF0FUUHkNJxhLZfEJNvol06tzwrgd
                LbXsFZYmSMPnHLB+zNJFbq15+SOf50+6rG7lKOjwV1ibGdhHYRVYVJ9Wn
                k2HWtLdIWMSH9lfyODZoZTb4xdnpxQSEF9oyOWIqp6gaI9pI1Qo7BijbF
                ZkoaAtEeiiLeKn72xM7vMZofJy8zJys2UxsCT3kO229LH1tXAAAOw=="

    :return: str 保存到本地的文件名
    """
    # 1、信息提取
    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
    if result:
        ext = result.groupdict().get("ext")
        data = result.groupdict().get("data")

    else:
        raise Exception("Do not parse!")

    # 2、base64解码
    img = base64.urlsafe_b64decode(data)

    # 3、二进制文件保存
    filename = "{}.{}".format(uuid.uuid4(), ext)
    with open(filename, "wb") as f:
        f.write(img)

    return filename


def pic_to_base64(path):
    """
    编码图片
    :param filename: str 本地图片文件名
    :return: str 编码后的字符串
        eg:
        src="data:image/gif;base64,R0lGODlhMwAxAIAAAAAAAP///
            yH5BAAAAAAALAAAAAAzADEAAAK8jI+pBr0PowytzotTtbm/DTqQ6C3hGX
            ElcraA9jIr66ozVpM3nseUvYP1UEHF0FUUHkNJxhLZfEJNvol06tzwrgd
            LbXsFZYmSMPnHLB+zNJFbq15+SOf50+6rG7lKOjwV1ibGdhHYRVYVJ9Wn
            k2HWtLdIWMSH9lfyODZoZTb4xdnpxQSEF9oyOWIqp6gaI9pI1Qo7BijbF
            ZkoaAtEeiiLeKn72xM7vMZofJy8zJys2UxsCT3kO229LH1tXAAAOw=="

    """
    # 1、文件读取
    ext = path.split(".")[-1]

    with open(path, "rb") as f:
        img = f.read()

    # 2、base64编码
    data = base64.b64encode(img).decode()

    print(data)
    # 3、图片编码字符串拼接
    src = "data:image/{ext};base64,{data}".format(ext=ext, data=data)
    return src


if __name__ == '__main__':
    # 下载百度首页logo保存到本地 baidu.png
    # https://www.baidu.com/img/bd_logo1.png

    # 编码测试
    print(pic_to_base64('my-icon.ico'))
    # src = "data:image/png;base64,iVBORw0KGgoAAAA..."

    # 解码测试
    # print(decode_image(src))


#
# data:,<文本数据>
# data:text/plain,<文本数据>
# data:text/html,<HTML代码>
# data:text/html;base64,<base64编码的HTML代码>
# data:text/css,<CSS代码>
# data:text/css;base64,<base64编码的CSS代码>
# data:text/javascript,<Javascript代码>
# data:text/javascript;base64,<base64编码的Javascript代码>
# data:image/gif;base64,base64编码的gif图片数据
# data:image/png;base64,base64编码的png图片数据
# data:image/jpeg;base64,base64编码的jpeg图片数据
# data:image/x-icon;base64,base64编码的icon图片数据