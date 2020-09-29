import requests, json, time
import pymysql as py

# 爬取各分区代表up的视频信息

# mid = '777536'  # 动画/lex 1
# mid = '14110780'  # 动画/凉风 2
# mid = '32708587' #番剧/番剧茶会 3
# mid = '5293668' #国创/齐天大肾余潇洒 5
# mid = '11491546'  # 国创/猫耳FM 6
# mid = '486183'  # 音乐/排骨教主 7
# mid = '391679' #音乐/A路人 8
# mid = '116683' #舞蹈/咬人猫 9
# mid = '8366990' #舞蹈/欣小萌 10
# mid = '546195' #游戏/老番茄 11
# mid = '122879' #游戏/敖厂长 12
# mid = '517327498' #科技/罗翔说刑法 13
# mid = '37663924' #科技/硬核的半佛仙人 14
mid = '9824766'  # 生活/敬汉卿 15
# mid = '19577966' #生活/李子柒 16
# mid = '375375' #鬼畜/伊丽莎白鼠 17
# mid = '7714' #鬼畜/女孩为何穿短裙 18
# mid = '62540916' #时尚/周六野 19
# mid = '466272' #时尚/党妹 20
# mid = '455876411' #娱乐/巨石强森 21
# mid = '5970160' #搞笑/小潮院长 23
# mid = '8969156' #知识/小白测评 24
# mid = '203337614' #影视/开心嘴炮 25

cid_url = 'https://api.bilibili.com/x/player/pagelist?aid={0}&jsonp=jsonp'
# 视频cid号查询
video_info_url = 'https://api.bilibili.com/x/web-interface/view?aid={0}&cid={1}'
# 视频信息查询接
video_list_url = 'https://api.bilibili.com/x/space/arc/search?mid={0}&ps=30&tid=0&pn={1}&keyword=&order=pubdate&jsonp=jsonp'
# 视频列表查询

tlite = ['aid', 'mid', 'author', 'create_time', 'title', 'video_length', 'video_type',
         'view', 'comment', 'danmuku', 'share', 'coin', 'like', 'favorite']


# 表单结构


def get_request(url):
    while True:
        try:
            data = requests.get(url)
            break
        except Exception as e:
            print(e)
            time.sleep(3)
    return data


def get_cid(aid):
    url = cid_url.format(aid)
    data = get_request(url)
    data = json.loads(data.text)
    cid = data['data'][0]['cid']
    return cid


def write_data(info):
    insert_table = '''insert into vidio_info15(aid, mid, author, create_time, title, video_length, video_type, 
         view_time, comment, danmaku, share, coin, dianzan, favorite)
         values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');
    ''' % (
        info['aid'], info['mid'], info['author'], info['create_time'], info['title'],
        info['length'],
        info['typeid'], info['view'], info['comment'], info['danmaku'], info['share'],
        info['coin'], info['like'],
        info['favorite'])
    cursor.execute(insert_table)


def processce_info(vlist):
    try:
        for v in vlist:
            info = {}
            aid = v['aid']
            cid = get_cid(aid)
            time.sleep(3)
            url = video_info_url.format(aid, cid)
            video_info1 = get_request(url)
            video_info = json.loads(video_info1.text)
            k = video_info['data']['stat']  # 获取视频详细信息
            timeArray = time.localtime(v['created'])
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            info['aid'] = aid
            info['mid'] = mid
            info['author'] = v['author']  # 视频作者
            info['create_time'] = create_time  # 视频发布时间
            info['title'] = v['title'].replace('\n', ' ')  # 视频标题
            info['length'] = v['length']  # 视频长度
            info['typeid'] = v['typeid']  # 视频类型
            info['view'] = k['view']  # 播放数量
            info['comment'] = v['comment']  # 评论数量
            info['danmaku'] = k['danmaku']  # 弹幕数量
            info['share'] = k['share']  # 分享数量
            info['coin'] = k['coin']  # 投币数量
            info['like'] = k['like']  # 点赞数量
            info['favorite'] = k['favorite']  # 收藏数量
            write_data(info)
    except Exception as e:
        raise e


def get_video_list():
    try:
        url = video_list_url.format(mid, 1)
        print(url)
        video_list_info = requests.get(url)
        video_list_info = json.loads(video_list_info.text)
        data = video_list_info.get('data')
        count = data['page']['count']  # 获取页数
        number = int(count / 30) + 1
        for i in range(number):
            url = video_list_url.format(mid, i + 1)
            video_list_info = get_request(url)
            video_list_info = json.loads(video_list_info.text)
            vlist = video_list_info['data']['list']['vlist']  # 获取视频简要内容
            print('write data : ', i)
            if not vlist:
                continue
            processce_info(vlist)
        print('end............')
    except Exception as e:
        raise e


if __name__ == "__main__":
    conn = py.connect("localhost", "root", "root", "test", charset='utf8')
    cursor = conn.cursor()
    create_table = '''create table if not exists vidio_info15(
                    aid varchar(20) PRIMARY KEY ,
                    mid varchar(20),
                    author varchar(20),
                    create_time varchar(50),
                    title varchar(200),
                    video_length varchar(10),
                    video_type varchar(10),
                    view_time varchar(100),
                    comment varchar(100),
                    danmaku varchar(100),
                    share varchar(100),
                    coin varchar(100),
                    dianzan varchar (100),
                    favorite varchar(100));
                    '''
    cursor.execute(create_table)

    get_video_list()

    conn.commit()
    cursor.close()
    conn.close()
