import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.pyplot import MultipleLocator

df=pd.read_excel("data.xlsx")
indicator = df.columns.tolist()  ##指标个数
project = df.index.tolist()
value = df.values

# print(data.iloc[8:12])
# print(data.iloc[0])
# print(data.iloc[4])
# print(data.iloc[7])
lable_list = ['Biodiversity','Distance to urban community','Weather index','Economy']
color_list = ['#fa7f7f','#facf5a','#6bc5d2','#a0e4b0']

# plt.subplot(2, 2, 1)
# plt.plot(data.iloc[0].tolist(), data.iloc[8], color='green', label='Total Score')
# plt.legend() # 显示图例
#
# plt.subplot(2, 2, 2)
# plt.plot(data.iloc[0].tolist(), data.iloc[9], color='red', label='light pollution')
# plt.legend() # 显示图例
#
# plt.subplot(2, 2, 3)
# plt.plot(data.iloc[0].tolist(), data.iloc[10],  color='skyblue', label='nature')
# plt.legend() # 显示图例
#
# plt.subplot(2, 2, 4)
# plt.plot(data.iloc[0].tolist(), data.iloc[11], color='blue', label='Humanities')
# plt.legend() # 显示图例

for i in range(4):
    data = df.sort_values(by=lable_list[i] , ascending=False)
    data = data.T
    plt.subplot(2 , 2 , i+1)
    plt.bar(data.iloc[1].tolist() , data.iloc[i+2] , color=color_list[i] , label=lable_list[i])
    print(data.iloc[i+2].name)
    plt.legend(loc = 9)  # 显示图例
    plt.tight_layout() #设置默认的间距
    #plt.subplots_adjust(wspace =1, hspace =1)#调整子图间距
    #plt.subplots_adjust( wspace =1)#调整子图间距
    plt.xlabel('location number',fontdict={'family' : 'Times New Roman', 'size'   : 16})
    plt.ylabel('',fontdict={'family' : 'Times New Roman', 'size'   : 16})
    plt.yticks([])  # 不显示y轴
    x_major_locator=MultipleLocator(1)
    # #把x轴的刻度间隔设置为1，并存在变量里
    # y_major_locator=MultipleLocator(10)
    #把y轴的刻度间隔设置为10，并存在变量里
    ax=plt.gca()

    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # #把x轴的主刻度设置为1的倍数
    # ax.yaxis.set_major_locator(y_major_locator)
    #把y轴的主刻度设置为10的倍数
    ax2 = ax.twinx()  # 创建共用x轴的第二个y轴

    color = 'tab:blue'
    #ax2.set_ylabel('Artificial Light Sources rate')
    ax2.plot(data.iloc[1].tolist() , data.iloc[6] , color='#872341' , label='Luminous Intensity')

    ax3 = ax2.twinx()

    ax3.plot(data.iloc[1].tolist() , data.iloc[7] , color='#f02a71' , label='The Ratio of Luminance')
    ax2.legend(prop={'family': 'Times New Roman' , 'size': 10})  # 显示图例
    #ax3.legend(prop={'family': 'Times New Roman' , 'size': 10})  # 显示图例
plt.show()