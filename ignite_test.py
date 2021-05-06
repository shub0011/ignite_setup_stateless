# pip3 install pyignite

from pyignite import Client

client = Client()
client.connect('http://acac441c23e0f47aebbcdc165ae3aedc-237846483.ap-south-1.elb.amazonaws.com', 10800)

#Create cache
my_cache = client.create_cache('my cache')

#Put value in cache
my_cache.put(1, 'Hello World')

#Get value from cache
result = my_cache.get(1)
print(result)