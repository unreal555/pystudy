from netCDF4 import Dataset
import netCDF4 as nc
import csv

dataset = Dataset(r'./cru_ts4.04.1901.2019.pet.dat.nc',mode='r',format="NETCDF4")
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
time = dataset.variables['time']
pet = dataset.variables['pet']
print(dataset.variables.keys())
print(time)
print(pet)


for t in time:
    for lat in lats:
        for lon in lons:
            try:
                print(nc.num2date(t,'hours since 1900-01-01 00:00:0.0'),lat,lon,pet[lat,lon,t])

            except Exception as e:
                pass


