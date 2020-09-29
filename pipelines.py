# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql as py
import redis

from bilibilispider.items import Up_Info, Area_Heat, Little_Area_Heat, Heat_Trend, Little_Heat_Trend, User_Info


class BilibilispiderPipeline:

    def __init__(self):
        pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024, db=0)
        # 创建连接对象，定位到db1
        conn = redis.Redis(connection_pool=pool)
        self.redis_conn = conn

    def process_item(self, item, spider):
        if isinstance(item, Up_Info):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists fans_hundred_info(
            area varchar(20),
            name varchar(50) ,
            fans_num varchar(20) primary  key
            );
                        '''
            cursor.execute(create_table)
            insert = '''
                        insert into fans_hundred_info(area,name,fans_num
                        ) values
                        ('%s','%s','%s');
                        ''' % (item['area'], item['name'], item['fans_num'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()

        elif isinstance(item, Area_Heat):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists area_heat_info(
                        area varchar(20),
                        name varchar(200) primary key,
                        view_time varchar(20) 
                        );
                                    '''
            cursor.execute(create_table)
            insert = '''
                                    insert into area_heat_info(area,name,view_time
                                    ) values
                                    ('%s','%s','%s');
                                    ''' % (item['area'], item['name'], item['view_time'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()

        elif isinstance(item, Little_Area_Heat):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists little_area_heat_info(
                                    area varchar(20),
                                    little_area varchar(20),
                                    name varchar(200) primary key,
                                    view_time varchar(20) 
                                    );
                                                '''
            cursor.execute(create_table)
            insert = '''
                                                insert into little_area_heat_info(area,little_area,name,view_time
                                                ) values
                                                ('%s','%s','%s','%s');
                                                ''' % (
                item['area'], item['little_area'], item['name'], item['view_time'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()

        elif isinstance(item, Heat_Trend):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists heat_trend_info20200603(
                                    area varchar(20),
                                    name varchar(200) ,
                                    time varchar (200) ,
                                    view_time varchar(20) 
                                    );
                                                '''
            cursor.execute(create_table)
            insert = '''
                                                insert into heat_trend_info20200603(area,name,time,view_time
                                                ) values
                                                ('%s','%s','%s','%s');
                                                ''' % (
                item['area'], item['name'], item['time'], item['view_time'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()

        elif isinstance(item, Little_Heat_Trend):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists little_heat_trend_info20200603(
                                    area varchar(20),
                                    little_area varchar (20),
                                    name varchar(200) ,
                                    time varchar (200) ,
                                    view_time varchar(20) 
                                    );
                                                '''
            cursor.execute(create_table)
            insert = '''
                                                insert into little_heat_trend_info20200603(area,little_area,name,time,view_time
                                                ) values
                                                ('%s','%s','%s','%s','%s');
                                                ''' % (
                item['area'], item['little_area'], item['name'], item['time'], item['view_time'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()

        elif isinstance(item, User_Info):
            conn = py.connect("localhost", "root", "root", "test")
            cursor = conn.cursor()
            create_table = '''create table if not exists user_info(uid varchar(200),
                                                name varchar(200),
                                                space varchar(200),
                                                sex varchar(200),
                                                birthday varchar(200),
                                                address varchar(200),
                                                level varchar(200)
                                                );
                                                            '''
            cursor.execute(create_table)
            insert = '''
                        insert into user_info(
                        uid,name,space,sex,birthday,address,level
                         ) values
                         ('%s','%s','%s','%s','%s','%s','%s');
                         ''' % (item['uid'], item['name'], item['space'], item['sex'], item['birthday'],
                                item['address'], item['level'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()
