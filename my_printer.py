import time

def my_print(item,roll=False,timer=1):

    if roll:
        if isinstance(item, str):
            print('\r', item,end='',flush=True)
        if isinstance(item, (list, tuple)):
            for i in item:
                print('\r', i,end='', flush=True)
                time.sleep(timer)
    else:
        if isinstance(item,str):
            print(item)
        if isinstance(item,(list,tuple)):
            for i in item:
                print(i)

def my_print_waitting(style='X',timer=0.3):

    if style=='X':
        key=('一','＼','｜','／')
    if style=='.':
        key=('.','..','...','....','.....','......')
    if style=='*':
        key = ('*', '**', '***', '****', '*****', '******')

    while True:
        my_print(key,roll=True,timer=timer)

item=['adsfasdfasdf1','adsfasdfasdf2','adsfasdfasdf3','adsfasdfasdf4','adsfasdfasdf5','adsfasdfasdf6',]

# my_print(item,roll=True)
my_print_waitting(style='*')
    
