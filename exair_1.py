import requests
serviceKey='http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc'
url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : 'json', 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'year' : '2020', 'itemCode' : 'PM10' }
response = requests.get(url, params=params)
print(response.next)
