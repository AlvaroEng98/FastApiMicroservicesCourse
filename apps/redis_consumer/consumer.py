from apps.core.redis_client import redis_conn

key = 'order_completed'
group = 'inventory-group'

try:
    redis_conn.xgroup_create(key,group)
except:
    print('Group all ready exist!!')

while True:
    try:
        results = redis_conn.xreadgroup(group, key, {key : '>'}, None)

        print(results)
    except Exception as e:
        print(str(e))