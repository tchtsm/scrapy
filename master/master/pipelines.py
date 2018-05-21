import redis

class MasterPipeline(object):

    def __init__(self):
        self.redis_url = 'redis://123456:@localhost:6379/'
        self.r = redis.Redis.from_url(self.redis_url,decode_responses=True)

    def process_item(self, item, spider):
        self.r.lpush('myredis:start_urls', item['url'])