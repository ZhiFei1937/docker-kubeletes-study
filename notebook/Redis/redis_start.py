import redis

def test():
    pool = redis.ConnectionPool(host='192.168.43.179',port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('name1','lili')
    print(r.get('name1'))
if __name__ == '__main__':
    test()