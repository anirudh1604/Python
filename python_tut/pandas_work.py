import pandas as pd
df=pd.read_csv('nyc_weather.csv')
print(df['Temperature'].max())
print(df['EST'][df['Events']=='Rain'])
print(df.shape)
print(df.head())
print(df.tail())
mf=df[df.Temperature==df.Temperature.max()]
print(mf)
mf.to_csv('new_csv.csv')
g=df.groupby('Events')
print(g)

for events, events_df in g :
    print(events)
    print(events_df)


print(g.max())



us_weather=pd.DataFrame( {
"city":["new york","chicago","buffalo"],
"temperature" :[21,14,35],
"humidity":[68,65,75]
}
)
print(us_weather)
india_weather=pd.DataFrame( {
"city":["mumbai","delhi","lucknow"],
"temperature" :[21,44,46],
"humidity":[68,72,59]
}
)
print(india_weather)

data=pd.concat([india_weather,us_weather])
data1=pd.concat([us_weather,india_weather])
print(data)
print(data1)
data_axis=pd.concat([india_weather,us_weather],axis=1)
print(data_axis)
