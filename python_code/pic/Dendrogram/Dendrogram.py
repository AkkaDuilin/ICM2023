# Libraries
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram , linkage
import numpy as np

# Import the mtcars dataset from the web + keep only numeric variables
url = 'https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'

df = pd.read_csv('D:\ICM2023\python_code\data processing\Dendrogram_value.csv' , encoding='gb18030' , index_col=0)
# path = 'D:\ICM2023\python_code\entropy weight\data - 副本.csv'
# df = pd.read_csv(path)
print(df)
# df = df.set_index('model')
#df = df.reset_index(drop=True)
df.head()
print(df)
# Calculate the distance between each sample You have to think about the metric you use (how to measure similarity) +
# about the method of clusterization you use (How to group cars)
Z = linkage(df, 'ward')

# Plot title
plt.title('Dendrogram')

# Plot axis labels
plt.xlabel('location',fontdict={'family' : 'Times New Roman', 'size'   : 1})
plt.ylabel('distance (Ward)',fontdict={'family' : 'Times New Roman', 'size'   : 20})
plt.xticks(rotation=90)

# Make the dendrogram
with plt.rc_context({'lines.linewidth': 3.0}):
    dendrogram(Z, labels=df.index, leaf_rotation=90)

# Show the graph
plt.show()
