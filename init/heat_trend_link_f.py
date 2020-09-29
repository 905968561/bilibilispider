import redis

# 分区热度趋势
pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
# 创建连接对象
conn = redis.Redis(connection_pool=pool)
print("start...")
dlist = ['20190724', '20190924', '20191124', '20200124', '20200403', '20200603']
list = ['1', '13', '167', '3', '129', '4', '36', '160', '119', '155', '165', '5', '11', '23']
url = "https://www.kanbilibili.com/daily/" + dlist[5] + "?typeid={}&orderby=play&copyright=0"  # 选择爬取时间
for i in range(len(list)):
    url1 = url.format(list[i])
    conn.lpush("job:start_url", url1)
print("end...")
