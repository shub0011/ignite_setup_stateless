import grequests
import requests
import base64
import json

urls = []

# url = 'http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite?cmd=top'
# url = "http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite\?cmd\=put\&key\=key{}\&val\=shubhendu{}\&cacheName\=test3"
url = "http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite"
count = 0

payload = {} 
headers = {}
query = {'cmd':'get', 'key':'key','cacheName':'test3'}
responses = []
count=1
input =100
for i in range(input):
    
    count = count+1
    query['key']="key__"+str(i)
    print (i)
    rs = (requests.get(url, params=query))
    output = rs.__dict__['_content'].decode('utf-8')
    result = json.loads(output)
    responses.append(result['response'])
# response_list= grequests.map(rs)

# print (response_list)

print (responses)
print('total values called : '+ str(input))
print('total values printed : ' +str(len(responses)))
# print (response_list)
