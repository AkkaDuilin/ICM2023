# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df1 = pd.DataFrame({
    'group': ['Old' , 'Now'] ,

    'RL': [14.72,13.45] ,
    'DUC': [6.96,6.37],

    'BI': [7.54,6.75] ,
    'LI': [33.19,30.35] ,
    'WI': [8.61,7.91] ,
    'EI': [28.95,26.66] ,

})
df2 = pd.DataFrame({
    'group': ['Old' , 'Now'] ,

    'RL': [14.73,12.40] ,
    'DUC': [6.97,5.88],

    'BI': [7.54,6.75] ,
    'LI': [33.19,27.95] ,
    'WI': [8.61,7.42] ,
    'EI': [28.95,23.63] ,

})

df = pd.DataFrame({
    'group': ['Old' , 'Now'] ,

    'RL': [11.73 , 6.35] ,
    'DUC': [50.25 , 50.25],

    'BI': [46.68 , 41.75] ,
    'LI': [53.47 , 42.89] ,
    'WI': [0.1 , 0.1] ,
    'EI': [0.1 , 0.1] ,

})
df_X = pd.DataFrame({
    'group': ['Old' , 'Now'] ,

    'RL': [61.53 , 51.81] ,

    'DUC': [93.63 , 93.63],
    'BI': [100.06 , 100.06] ,
    'LI': [100.10 , 84.29] ,
    'WI': [100.10 , 100.10] ,
    'EI': [100.01 , 100.01] ,

})

# ------- PART 1: Create background

# number of variable
categories = list(df)[1:]
print(categories)
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111 , polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1] , categories,fontdict={'family' : 'Times New Roman', 'size'   : 20,'weight': 'bold'})
plt.xlabel('Xinjiekou',fontdict={'family' : 'Times New Roman', 'size'   : 27,'weight': 'bold'})
plt.ylabel('',fontdict={'family' : 'Times New Roman', 'size'   : 16})
# Draw ylabels
ax.set_rlabel_position(0)
# ,70,80,90,100
# ,"70","80","90","100"
plt.yticks([10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100 , 110] ,
           ["10" , "20" , "30" , "40" , "50" , "60" , "70" , "80" , "90" , "100" , ""] , color="grey" , fontdict={'family' : 'Times New Roman', 'size'   : 15,'weight': 'bold'})
# plt.ylim(0 , 35)


# plt.yticks([10 , 20 , 30 , 40 , 50 , 60 ] ,
#            ["10" , "20" , "30" , "40" , "50" ,'' ] , color="grey" , fontdict={'family' : 'Times New Roman', 'size'   : 15,'weight': 'bold'})

# ------- PART 2: Add plots

# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable

# Ind1
values = df.loc[0].drop('group').values.flatten().tolist()
print(values)
values += values[:1]
ax.plot(angles , values , linewidth=1 , linestyle='solid' , label="Measures not implemented")
ax.fill(angles , values , '#95e1d3' , alpha=0.5)
# for a, b in zip(angles, values):
#     ax.text(a, b+5, '%.1f' % b, fontsize=12, color='#888e7e')

# Ind2
values = df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles , values , linewidth=1 , linestyle='solid' , label="Implementation measures")
ax.fill(angles , values , '#f38181' , alpha=0.5)
# for a, b in zip(angles, values):
#     ax.text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='#888e7e')

# Add legend
plt.legend(loc='upper right' , bbox_to_anchor=(0.1 , 0.1),prop={'family' : 'Times New Roman', 'size'   : 30,'weight': 'bold'})

# Show the graph
plt.show()
