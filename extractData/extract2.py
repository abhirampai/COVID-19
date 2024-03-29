import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from folium import Choropleth, Circle, Marker,IFrame
from folium.plugins import HeatMap, MarkerCluster
import math
import json

country_geo = pd.read_csv('../Data/india-states.geo.csv')
data = pd.read_csv('../Data/data.csv')
data1= pd.read_csv('../Data/data1.csv')
merged = data.merge(data1, on='stateData',how='left')
print(merged) 
merged=merged.rename(index=str,columns={"stateData": "province"})
df1 = pd.DataFrame(merged,columns=['province', 'Indian','Foreign','discharged_y','deaths_y','helpline','cases'])
df1=df1.fillna(0)
print(df1)
df2 = pd.DataFrame(merged,columns=['province', 'Indian','Foreign','discharged_y','deaths_y','helpline'])
df2=df2.fillna(0)
df2.to_excel("../Data/output1.xlsx") 
merged = country_geo.merge(df1, on='province') 

m_3 = folium.Map(location=[20.5937,78.9629], tiles='CartoDB dark_matter', zoom_start=2)

mc = MarkerCluster()
for idx, row in merged.iterrows():
    if not math.isnan(row['cases']) and not math.isnan(row['cases']):
        location=[row['LAT'],row['LON']]
        popup='<div style="width:300">'+'<STRONG>'+'<h3>'+row['province']+'</h3>'+'<br>'+'<p>'+'Confirmed Indian National-'+str(int((row['Indian'])))+'</p>'+'<br>'+'<p>'+'Confirmed Foreign National-'+str(int((row['Foreign'])))+'</p>'+'<br>'+'<p>'+'Deaths-'+str(int((row['deaths_y'])))+'</p>'+'<br>'+'<p>'+'Discharged-'+str(int(row['discharged_y']))+'</p>'+'<br>'+'<p>'+'Helpline-'+str(row['helpline'])+'</p>'+'</STRONG>'+'</div>'
        mc.add_child(Marker(location=location,popup=popup))

m_3.add_child(mc)
m_3.save("../index1.html")
m_3