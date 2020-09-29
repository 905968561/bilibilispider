import redis

# 小分区热度趋势
pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
# 创建连接对象
conn = redis.Redis(connection_pool=pool)
print("start...")
dlist = ['20190724', '20190924', '20191124', '20200124', '20200403', '20200603']
list = ['1', '13', '167', '3', '129', '4', '36', '160', '119', '155', '165', '5', '11', '23']
list1 = ['24', '25', '27', '47']  # 动画 1 MAD 24  MMD 25 综合 27 短片 47
list2 = ['32', '33', '51', '152']  # 番剧 13 完结 32 连载 33 资讯 51 官方衍生 152
list3 = ['153', '168', '169', '170']  # 国创 167 国产 153 国产原创 168 布袋戏 169 资讯 170
list4 = ['28', '29', '30', '31', '54', '59', '130']  # 音乐 3 原创 28 三次元音乐 29 vocaloid 30 翻唱 31 OP/ED 54 演奏 59 音乐选集 130
list5 = ['20', '154', '156']  # 舞蹈 129 宅舞 20 三次元舞蹈 154 舞蹈教程 156
list6 = ['17', '19', '65', '121', '136', '171', '172',
         '173']  # 游戏 4 单机游戏 17 mugen 19 网络游戏 65 GMV 121 音游 136 电子竞技 171 手机游戏 172 桌游棋牌 173
list7 = ['37', '95', '122', '124']  # 科技 36 纪录片 37 数码 95 野生技术学会 122 趣味科普人文 124
list8 = ['21', '75', '76', '138', '161', '162', '163']  # 生活 160 日常 21 动物圈 75 美食圈 76 搞笑 138 手工 161 绘画 162 运动 163
list9 = ['22', '26', '126', '127']  # 鬼畜 119 鬼畜调教 22 音mad 26 人力vocaloid 126 教程演示 127
list10 = ['157', '158', '159', '164']  # 时尚 155 美妆157 服饰 158 咨询159 健身 164
list11 = ['71', '131', '137']  # 娱乐 5 综艺 71 korea相关 131 明星 137
list12 = ['83', '146']  # 电影 23 其他国家 83  日本电影 146

url = "https://www.kanbilibili.com/daily/" + dlist[5] + "?typeid={}&orderby=play&copyright=0"  # 选择爬取时间
for i in range(len(list1)):
    url1 = url.format(list1[i])
    conn.lpush("job:start_url", url1)
for i in range(len(list2)):
    url2 = url.format(list2[i])
    conn.lpush("job:start_url", url2)
for i in range(len(list3)):
    url3 = url.format(list3[i])
    conn.lpush("job:start_url", url3)
for i in range(len(list4)):
    url4 = url.format(list4[i])
    conn.lpush("job:start_url", url4)
for i in range(len(list5)):
    url5 = url.format(list5[i])
    conn.lpush("job:start_url", url5)
for i in range(len(list6)):
    url6 = url.format(list6[i])
    conn.lpush("job:start_url", url6)
for i in range(len(list7)):
    url7 = url.format(list7[i])
    conn.lpush("job:start_url", url7)
for i in range(len(list8)):
    url8 = url.format(list8[i])
    conn.lpush("job:start_url", url8)
for i in range(len(list9)):
    url9 = url.format(list9[i])
    conn.lpush("job:start_url", url9)
for i in range(len(list10)):
    url10 = url.format(list10[i])
    conn.lpush("job:start_url", url10)
for i in range(len(list11)):
    url11 = url.format(list11[i])
    conn.lpush("job:start_url", url11)
for i in range(len(list12)):
    url12 = url.format(list12[i])
    conn.lpush("job:start_url", url12)
print("end...")
