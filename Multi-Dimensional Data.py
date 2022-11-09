import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
from cartopy import feature as cf

# read datadata.precip.sel(time='1981-01-01').plot(cmap='virdis')
data = xr.open_dataset("chirps_21_WA_new.nc")
data

fig = plt.figure()
ax = fig.add_subplot(111, projection = ccrs.PlateCarree())
data.precip.sel(time = '1981-01-01').plot(cmap='hot',add_colorbar = False)
# add feature
ax.add_feature(cf.BORDERS,lw = 3,color = 'r')


data
ds = data.precip.sel(time=slice('2010-01-01','2021-12-31'))
ds_year=ds.groupby('time.year').sum()
ds_year
dd=data.precip.sel(longitude=0.5,latitude=8,method='nearest').plot()
dm = ds_year.sel(year = slice(2010,2013))
dm
dm.plot(x = 'longitude',y = 'latitude', col = 'year', col_wrap=2,cmap= 'jet_r')

dm.sum('year').plot(cmap = 'twilight_r')
plt.title('asta')
plt.xlabel('longitude')
plt.ylabel('latitude')

dm_seas = ds.groupby('time.season').mean()
dm_seas
dm_seas.plot(x = 'longitude',y = 'latitude', col = 'season', col_wrap=1,cmap= 'jet')
dm_seas.sel(season = 'DJF').plot(cmap='jet_r')
dm_seas.sel(season =['DJF','MAM']).plot(x = 'longitude',y = 'latitude', col = 'season', col_wrap=2,cmap= 'jet_r')
dm_seas.sel(season = slice('JJA','SON')).plot(x = 'longitude',y = 'latitude', col = 'season', col_wrap=2,cmap= 'jet')
ds_month = ds.groupby('time.month').mean()
ds_month.plot(x = 'longitude',y = 'latitude', col = 'month', col_wrap=6,cmap= 'jet_r')
ds_month.sel(month=[4,7,10,12]).plot(x = 'longitude',y = 'latitude', col = 'month', col_wrap=2,cmap= 'jet')
ds_month.sel(longitude=0.35,latitude=6.5, method='nearest').plot()
ds_month.mean(dim =['longitude','latitude']).plot()
