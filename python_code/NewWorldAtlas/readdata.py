from osgeo import gdal
import pandas as pd
import numpy as np

gdal.AllRegister()
filename_list = ['World_Atlas_2015.tif', 'GEDI04_B_MW019MW138_02_002_05_R01000M_MU.tif' ,
                 'gpw_v4_population_density_rev11_2015_2pt5_min.tif' ]
find_list = {'Nanjing Xinjiekou area': [32.0 , 118.0] , 'Fengxian District': [30.0 , 121.0] ,
             'Yellowstone Park': [44.3 , -110.3] , 'Fresno city': [37.0 , -119.0] , 'Chesterbrook': [41.1 , -77.1] ,
             'Manhattan': [40.0 , -74.0] , 'jiuzhaigou': [33.1 , 104.1] , 'Xiaogang Village': [32.2 , 117.7]}

# for key in find_list.keys():
#     print('find ans of ' + key)
for filename in filename_list:
    filePath = r'D:\ICM2023\python_code\NewWorldAtlas/' + filename
    dataset = gdal.Open(filePath)
    adfGeoTransform = dataset.GetGeoTransform()
    nXSize = dataset.RasterXSize  # x
    nYSize = dataset.RasterYSize  # y
    print(nXSize , nYSize)
    im_data = dataset.ReadAsArray(0 , 0 , nXSize , nYSize)
    index = []  # loc
    columns = []  # iloc
    for j in range(nYSize):
        lat = adfGeoTransform[3] + j * adfGeoTransform[5]
        index.append(lat)
    for i in range(nXSize):
        lon = adfGeoTransform[0] + i * adfGeoTransform[1]
        columns.append(lon)
    data = pd.DataFrame(im_data , index=index , columns=columns)
    data.where(data >= 0 , data - data , inplace=True)
    print(filename + ' read done')
    for i in data.index:
        if -90 < i < 90:
            pass
        else:
            i = i / 100000

        data.rename(index={i: int(i)} , inplace=True)

    for j in data.columns:
        if -180 < j < 180:
            pass
        else:
            j = j / 100000

        data.rename(columns={j: int(j)} , inplace=True)

    print(data)

    for key in find_list.keys():
        print('find ans of ' + key)
        x = find_list[key][0]
        y = find_list[key][1]
        key_data = data.loc[(x,y)]
        print(key_data)
        key_data.to_csv(key+filename+'.csv')

