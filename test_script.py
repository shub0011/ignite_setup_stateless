import grequests
import requests

urls = []

# url = 'http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite?cmd=top'
# url = "http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite\?cmd\=put\&key\=key{}\&val\=shubhendu{}\&cacheName\=test3"
url = "http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com:8080/ignite"
count = 0

payload = {} 
headers = {}
query = {'cmd':'put', 'key':'key','cacheName':'test3','val':'value'}
responses = []
count=1
for i in range(100):
    
    count = count+1
    query['key']="key__"+str(i)
    query['val']="value__"+str(i)
    print (i)
    rs = (requests.get(url, params=query))
    responses.append(rs)
# response_list= grequests.map(rs)

# print (response_list)

print (responses)
# print (response_list)




