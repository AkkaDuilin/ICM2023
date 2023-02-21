# import the library
import folium
# Import the pandas library
import pandas as pd


# Make an empty map
m = folium.Map(location=[20,0], tiles='Stamen Terrain', zoom_start=2)


# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[104.14,117.71,121.47,118.46,-110.30,-119.00,-77.11,-74.00,110.26,103.49,104.55,116.06,-77.29,-115.13],
   'lat':[33.16,32.28,30.92,32.02,44.36,37.00,41.12,40.00,29.18,36.03,24.58,39.01,42.85,36.18],
  # 'name':['jiuzhaigou', 'Xiaogang Village', 'Fengxian District, Shanghai', 'Nanjing Xinjiekou area', 'Yellowstone Park', 'Fresno city, California', 'Chesterbrook, PA', 'Manhattan, New York','Zhangjiajie National Forest Park','Chengguan District, Lanzhou City','Nahui Village, Qianxinan Prefecture','Xiongan New District','Ontario County, New York','Internalized Las Vegas, DA'],
   'name':[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
}, dtype=str)

print(data)

#for i in range(0,len(data)):
   # folium.Marker(
   #     location=[data.iloc[i]['lat'] , data.iloc[i]['lon']] ,
   #     popup=data.iloc[i]['name'] ,
   #     icon=folium.DivIcon(html=f"""<div style="font-family: courier new; color: red; font-size =
   #     180rpx; font-weight:bold; ">{data.iloc[i]['name']}</div>""")
   #
   # ).add_to(m)
for i in range(0,len(data)):
   folium.Marker(
       location=[data.iloc[i]['lat'] , data.iloc[i]['lon']] ,
       popup=data.iloc[i]['name'] ,
       icon=folium.Icon(color='red')
   ).add_to(m)


m.show_in_browser()
