import redis

# 分区热度
pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
# 创建连接对象
conn = redis.Redis(connection_pool=pool)
print("start...")
list = ['1', '13', '167', '3', '129', '4', '36', '160', '119', '155', '165', '5', '11', '23']
for i in range(14):
    url = "https://www.kanbilibili.com/all/20200722?typeid={}&orderby=play&copyright=0".format(list[i])
    conn.lpush("job:start_url", url)

print("end...")
