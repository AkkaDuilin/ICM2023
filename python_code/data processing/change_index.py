import numpy as np
import pandas as pd

data = pd.read_csv('GEDI04_B_MW019MW138_02_002_05_R01000M_MU.tif_no_avg.csv' , encoding='gb18030' , index_col=0)
for i in data.index:
    i = float(i)
    print(i,type(i))
    data.rename(index={i: i/100000} , inplace=True)
for j in data.columns:
    j_ = float(j)/100000
    print(j,type(j))
    data.rename(columns={j: j_} , inplace=True)

print(data)
data.to_csv('GEDI04_B_MW019MW138_02_002_05_R01000M_MU.csv')