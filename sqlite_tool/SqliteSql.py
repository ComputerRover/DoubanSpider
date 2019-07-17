import sqlite3


def create_db():
    conn = sqlite3.connect('E:\gitsCode\Code\python\DoubanSpider\db\doubanInfo.db')
    print('---数据库连接成功---')
    return conn


def create_table():
    cur = conn.cursor()
    # data_title - --电影名称
    # data_info - --电影信息（导演、主演、上映时间）
    # data_quote - --电影引言
    # data_score - --电影评分
    # data_num - --电影评论人数
    # data_picurl - --电影封面链接
    cur.execute('create table person (id integer primary key,name varchar(20),age integer )')


def select_sql():
    cur = conn.cursor()
    cur.execute('select * from douban_top250')
    res = cur.fetchall()
    for line in res:
        print(line)


def insert_sql():
    cur = conn.cursor()
    cur.executemany(' insert into douban_top250 values (?,?,?,?,?,?,?,?)', [(1, 'wew', 'wew', 'wew', 'wew', 'wew', 'wew', 'ss')])
    conn.commit()


conn = create_db()
insert_sql()
select_sql(conn)
