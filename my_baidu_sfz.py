from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = '23160961'
API_KEY = 'EQxxCuTCj20BWmS5ji2GwGB8'
SECRET_KEY = 'OW7NnVb2GoNXE0M4ySqmS9zTDR2yroZ7'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_id_card_info(id_card_path):
    with open(id_card_path, 'rb') as fp:
        image=fp.read()

    idCardSide = "front"

    """ 调用身份证识别 """
    client.idcard(image, idCardSide);

    """ 如果有可选参数 """
    options = {}
    options["detect_direction"] = "true"
    options["detect_risk"] = "false"

    """ 带参数调用身份证识别 """
    result=client.idcard(image, idCardSide, options)


    return result




s=get_id_card_info('./pic/sfz.jpg')

for key in s['words_result'].keys():
    i = s['words_result'][key]['words']
    print(key, i)
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(key + ':' + i + '\r\n')