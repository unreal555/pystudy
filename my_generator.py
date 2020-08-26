# coding: utf-8
# Team : JiaLiDun University
# Author：zl
# Date ：2020/8/10 0010 下午 5:08
# Tool ：PyCharm
import my_changliang

def createCounter():
    s = 0
    def counter():
        nonlocal s
        s = s + 1
        return s
    return counter


def get_execl_cell():
    for x,y in [[x,y] for y in range(1,1000) for x in my_changliang.DA_XIE_ZI_MU ]:
        yield x,y
              
if __name__ == '__main__':
    cell=get_execl_cell()
    for i in range(1,1000*26):
        try:
            x,y=next(cell)
        except StopIteration:
            break

        print(x,y)