import json

import requests

s = requests.get("https://api.bilibili.com/x/relation/followers?vmid=546195&pn=1&ps=100&order=desc&jsonp=jsonp")
user = json.loads(s.text)
data1 = user['data']['list'][0]['mid']
data2 = user['ttl']
print(data1)
# mid =123131
# url3 ="https://api.bilibili.com/x/relation/followers?vmid=546195&pn={}&ps=100&order=desc&jsonp=jsonp".format(mid)
# print(url3)
