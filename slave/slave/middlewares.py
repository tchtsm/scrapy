import random
from .useragent import agents

class UserAgentMiddleware(object):

    def process_request(self, request, spider):
        agent = random.choice(agents)
        referer = request.meta.get('referer', None)
        request.headers["User-Agent"] = agent
        request.headers["Referer"] = referer