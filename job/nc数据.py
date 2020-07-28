from netCDF4 import Dataset
import netCDF4 as nc
import csv
import os

column_names=['lat','lon','time','value']
dataset = Dataset(r'C:\Users\Administrator\Desktop/cru_ts4.04.1901.2019.pet.dat.nc',mode='r',format="NETCDF4")
result='./result.csv'

lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
time = dataset.variables['time']
pet = dataset.variables['pet']
print(dataset.variables.keys())
print(time)
print(pet)

def write_csv(file_path,item,column_names):
    '''
    :param file_path: 文件的全路径
    :param item:    要写入的元素,字典形式,key为column_names中的字段
    :param column_names:    表头
    :return:
    '''

    if os.path.exists(file_path):
        with open(file_path, 'a', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, column_names)
            writer.writerow(item)
            f.flush()

    else:
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
            # 若文件不存在,则创建文件,写入表头和数据,
            #标头在这里传入，作为第一行数据
            writer = csv.DictWriter(f, column_names)
            writer.writeheader()
            writer.writerow(item)
            f.flush()
    print('{} 写入成功'.format(item))
    return True



for t in time:
    for lat in lats:
        for lon in lons:
            try:
                time=nc.num2date(t, 'hours since 1900-01-01 00:00:0.0')
                value=pet[lat,lon,t]
                if  not value:
                    continue
                item=dict(lat=lat,lon=lon,time=str(time),value=float(value))
                print(item)
                write_csv(result, item, column_names)
            except Exception as e:
                print("错误,{}".format(e))


