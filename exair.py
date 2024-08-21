import requests

serviceKey='pmnW1arvVaGPOAKOXRBgWrPUZVjrJRSWm+vzEsWmvPJ1FeMyle9bgd1Em8ES/5VMIcCGPh3UG/lvz2TY3xBVNA=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
params ={'serviceKey' : 'json', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'searchDate' : '2020-11-14', 'InformCode' : 'PM10' }

response = requests.get(url, params=params)
print(response.text)
air=response,text
print(air['responce'][items])
print(air)