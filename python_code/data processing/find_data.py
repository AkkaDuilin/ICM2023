import numpy as np
import pandas as pd
import datatable as dt
from osgeo import gdal



def avg_arr ( df , num ):
    def sum_avg ( data , x , y , num ):
        copy_data = data.iloc[x:x + num , y:y + num]
        ans = sum(copy_data.sum()) / (num * num)

        return ans

    x = df.shape[0]
    y = df.shape[1]
    arr = pd.DataFrame(np.zeros((int(x / num) , int(y / num))))
    # print(arr)
    for i in range(int(x / num)):
        for j in range(int(y / num)):
            # print(sum_avg(df,i*num,j*num,num))
            arr.rename(index={i: data.index[i * num]} , inplace=True)
            arr.rename(columns={j: data.columns[j * num]} , inplace=True)
            arr.iloc[i , j] = sum_avg(df , i * num , j * num , num)
            pass
        print(i)
    return arr

def read_single_csv(input_path):
    import pandas as pd
    df_chunk=pd.read_csv(input_path,chunksize=1000)
    res_chunk=[]
    for chunk in df_chunk:
        res_chunk.append(chunk)
    res_df=pd.concat(res_chunk)
    return res_df


#natural = dt.fread('D:\ICM2023\python_code\entropy weight\GEDI04_B_MW019MW138_02_002_05_R01000M_MU.tif_avg.csv').to_pandas()

print('read done')
# light = read_single_csv('World_Atlas_2015.tif_no_avg.csv' )
light = dt.fread('D:\ICM2023\python_code\entropy weight\World_Atlas_2015.tif_no_avg.csv').to_pandas() #如果加.to_pandas 与pd.read_csv读取的数据格式一样
#population = dt.fread('D:\ICM2023\python_code\entropy weight\gpw_v4_population_density_rev11_2015_2pt5_min.tif_avg.csv').to_pandas()


# light = dt.fread('D:\ICM2023\python_code\entropy weight\china_avg.csv').to_pandas() #如果加.to_pandas 与pd.read_csv读取的数据格式一样

print('read done')
#population = read_single_csv('gpw_v4_population_density_rev11_2015_2pt5_min.tif_no_avg.csv' )
print('read done')
# gdp = pd.read_csv('GDP2005_1km.tif_no_avg.csv' , encoding='gb18030' , index_col=0)

find_list = {'九寨沟': [33.16 , 104.14] , '小岗村': [32.28 , 117.71] , '新街口': [32.02 , 118.46] , '奉贤区': [30.92 , 121.47] ,
             '黄石公园': [44.36 , -110.30] , '弗雷斯诺市': [37.00 , -119.00] , '切斯特布鲁克': [41.12 , -77.11] ,
             '曼哈顿': [40.00 , -74.00]}

# find_list = {'九寨沟': [33.16 , 104.14]}

csv_list = [light]
num = 0

for data in csv_list:
    num+=1

    for i in data.index[1:]:
        i_ = '%.2f' % float(i)
        data.rename(index={i: i_} , inplace=True)
    for j in data.columns[1:]:
        j_ = '%.2f' % float(j)
        print(num)
        data.rename(columns={j: j_} , inplace=True)
    print(data)
    for key in find_list.keys():
        x = find_list[key][0]
        y = find_list[key][1]
        ans = 0
        #print(data.index[1:],data.columns[1:])

        # for i in data.index[int(y*120+21600)-1000:int(y*120+21600)+1000]:
        #     for j in data.columns[int(-120*x+10200)-1000:int(-120*x+10200)+1000]:

        for i in data.index[1:]:
            for j in data.columns[1:]:
                # print(i,j)
                # print(data.at[i,"C0"],data.at[0,j])
                #print('%.1f' % data.at[i , "C0"] , '%.1f' % x , '%.1f' % data.at[0 , j] , '%.1f' % y)
                #print(data.at[i,j])
                if ('%.2f' % data.at[i,"C0"] =='%.2f' % x) and ('%.2f' % data.at[0,j] =='%.2f' % y):

                    ans += data.at[i,j]
                    #print(i , j,data.at[i,j])
                else:
                    pass
        print(key,ans)


# data = data.loc[data.index < 53.0 , data.columns < 135.0]
#     data = data.loc[data.index > 10.0 , data.columns > 73.0]
