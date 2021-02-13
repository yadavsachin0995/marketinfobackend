import redis

def redis_client():
    r = redis.Redis(
        host = '127.0.0.1',
        port = 6379
        )
    return r