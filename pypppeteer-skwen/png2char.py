import cv2
import numpy as np
import requests
import pickle
import os
import re


if __name__ == '__main__':


    
    if os.path.exists('png2char.dat'):
        with open('png2char.dat','rb') as f:
            png2char=pickle.load(f)
    else:
        png2char={}


    result={}
    for file in os.listdir('./a'):
        
        if os.path.isfile(file) and 'txt' in file:
            print(file)
            with open(file,'r',encoding='utf-8') as f:
                txt =f.read()            
                for pre_two_word,url,next_tow_word in re.findall('()<imgsrc="(.*?)">()',txt):
                    if url not in result.keys():
                        result[url]=[[pre_two_word,'???',next_tow_word] ]
                    else:
                        result[url].append([pre_two_word,'???',next_tow_word ])
    print(png2char)

                
    
    

    for i in result.keys():
        key=i.split('/')[-1]
        print(i,key)
        if key in png2char and png2char[key]!='':
            #print('跳过',png2char[key],result[i])
            continue
        
        else:
            r=requests.get(i)
            print(r)
            img = cv2.imdecode(np.frombuffer(r.content, np.uint8), cv2.IMREAD_COLOR)


            cv2.imshow('image', img) # 建立名为‘image’ 的窗口并显示图像
            k = cv2.waitKey(0) # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
            if k:     # 键盘上Esc键的键值
                cv2.destroyAllWindows()
            png2char[key]=input(result[i])


            

            
            while png2char[key]=='':
              
                cv2.imshow('image', img) # 建立名为‘image’ 的窗口并显示图像
                k = cv2.waitKey(0) # waitkey代表读取键盘的输入，括号里的数字代表等待多长时间，单位ms。 0代表一直等待
                if k:     # 键盘上Esc键的键值
                    cv2.destroyAllWindows()
    
                png2char[key]=input(result[i])
            
                
            with open('png2char.dat','wb') as f:
                pickle.dump(png2char,f)
    

                
    with open('yin窟魔语_精品小说_wslmd199061.txt','r',encoding='utf-8') as f:
        txt=f.read()


    for i in png2char.keys():
        s='''<imgsrc="http://m.skwen.me/wzbodyimg/{}">'''.format(i)
        t=png2char[i]
        txt=txt.replace(s,t)
    print(txt)
        
