from netCDF4 import Dataset
import netCDF4 as nc
import csv
import os
import re
import numpy as np
#from mpl_toolkits.basemap import Basemap      #pip install matplotlib 3.0.3
import matplotlib.pyplot as plt
import my_csv_tools

def write_csv(file_path,item,column_names):
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

shezhi=[2000]                   #数组为空,取全部,输入那年,取那年的数据    [1900,2000]
dataset = Dataset(r'z:/cru_ts4.04.1901.2019.pet.dat.nc',mode='r',format="NETCDF4")
result='./result.csv'

column_names=['lat','lon','time','value']

lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
time = dataset.variables['time'][:]
pet = dataset.variables['pet']

def to_csv():
    years=[]

    print(dataset.variables.keys())
    print(lats)
    print(lons)
    print(time)
    print(pet)

    years=[]

    if shezhi==[]:
        years=time
    else:
        for i in range(0,len(pet)):
            key = re.findall('\d{4}', str(nc.num2date(time[i], 'days since 1900-01-01 00:00:0.0')))
            if len(key) == 1:
                if int(key[0]) in shezhi:
                    years.append(i)

    print(years)


    for i in years:
        for lat in lats:
            for lon in lons:
                try:
                    value=pet[i,lat,lon]
                    if not value:
                        print('跳过空数据',i,str(nc.num2date(time[i], 'days since 1900-01-01 00:00:0.0')),str(lat),str(lon))
                        continue
                    item=dict(lat=float(lat),lon=float(lon),time=str(nc.num2date(time[i], 'days since 1900-01-01 00:00:0.0')),value=float(value))
                    print(item)
                    my_csv_tools.write_csv(result, item, column_names)
                except Exception as e:
                    print("错误,{}".format(e))




to_csv()
 















