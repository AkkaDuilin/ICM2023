import numpy as np
import pandas as pd

d = {1: pd.Series([1 , 2 , 3 , 4] , index=[1 , 2 , 3 , 4]) ,
     2: pd.Series([5 , 6 , 7 , 8] , index=[1 , 2 , 3 , 4])}
df = pd.DataFrame(d)
print(df)

#print(df.loc[ df.index > 2 , df.columns < 3])
df.rename(columns={2: 1} , inplace=True)
df.rename(index={2: 1} , inplace=True)
print(df.loc[(1,1)])
# print(df.index[0])

# print(df.iloc[0:1,0:1])
# df.iloc[0,0] = 4
# print(df.iloc[0,0])
# df1 = sum(df.sum())
# print(df1)


def avg_arr ( df , num ):
    def sum_avg ( data , x , y , num ):
        copy_data = data.iloc[x:x + num , y:y + num]
        ans = sum(copy_data.sum())
        return ans

    x = df.shape[0]
    y = df.shape[1]
    arr = pd.DataFrame(np.zeros((int(x / num) , int(y / num))))
    # print(arr)
    for i in range(int(x / num)):
        for j in range(int(y / num)):
            # print(sum_avg(df,i*num,j*num,num))
            arr.iloc[i , j] = sum_avg(df , i * num , j * num , num)
            pass
    return arr


arr = avg_arr(df , 2)
# print(arr)
