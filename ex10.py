import requests
city_name='울산'
API_key='2f338ff7b62f89203e1751cd3101f1e7'
limit=5
url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
data=res.json()
print(len(data))
lat=data[0]['lat']
lon=data[0]['lon']
print(lat,lon)
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
res=requests.get(url)
weather=res.json()
print(weather)
print(weather['weather'][0]['description'])
print('20706 김서영')