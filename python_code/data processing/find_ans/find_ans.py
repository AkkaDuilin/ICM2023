import numpy as np
import pandas as pd


data = pd.read_csv('find_ans.csv' , encoding='gb18030' , index_col=0)
indicator = data.columns.tolist()
project = data.index.tolist()
value = data.values
print(indicator)
print(project)
print(value)
data.head()



def std_data ( value , flag ):
    for i in range(len(indicator)):
        # print(flag[i])
        if flag[i] == '+':
            value[: , i] = (value[: , i] - np.min(value[: , i] , axis=0)) / (
                    np.max(value[: , i] , axis=0) - np.min(value[: , i] , axis=0)) + 0.001
        elif flag[i] == '-':
            value[: , i] = (np.max(value[: , i] , axis=0) - value[: , i]) / (
                    np.max(value[: , i] , axis=0) - np.min(value[: , i] , axis=0)) + 0.001
    # print(value)
    return value



flag = ["-" , "+" , "-" , "+" , "+" , "+"]
std_value = std_data(value , flag)
print(std_value)
std_value.round(3)
DF = pd.DataFrame(std_value)
DF.to_csv('value.csv')



def cal_weight ( indicator , project , value ):
    p = np.array([[0.0 for i in range(len(indicator))] for i in range(len(project))])
    # print(p)
    for i in range(len(indicator)):
        p[: , i] = value[: , i] / np.sum(value[: , i] , axis=0)

    e = -1 / np.log(len(project)) * sum(p * np.log(p))
    g = 1 - e
    w = g / sum(g)
    return w


w = cal_weight(indicator , project , std_value)
w = pd.DataFrame(w , index=data.columns , columns=['权重'])
print("#######weight:#######")
print(w)
w.to_csv('weight.csv')
score = np.dot(std_value , w).round(2)
score = pd.DataFrame(score , index=data.index , columns=['综合得分']).sort_values(by=['综合得分'] , ascending=False)
score.to_csv('score.csv')
print(score)
