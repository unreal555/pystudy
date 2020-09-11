def my_print(item,roll=False):

    if roll:
        if isinstance(item, str):
            print('\r', item,end='',flush=True)
            return
        if isinstance(item, (list, tuple)):
            for i in item:
                print('\r', i,end='', flush=True)
            return
        return False
    else:
        if isinstance(item,str):
            print(item)
            return
        if isinstance(item,(list,tuple)):
            for i in item:
                print(i)
            return
        return False




item=['adsfasdfasdf1','adsfasdfasdf2','adsfasdfasdf3','adsfasdfasdf4','adsfasdfasdf5','adsfasdfasdf6',]

my_print(item,roll=True)
    
