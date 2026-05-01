from redis_om import get_redis_connection
from apps.core.config import settings

redis_conn = get_redis_connection(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PASSWORD or None,
    db=settings.REDIS_DB,
    decode_responses=True,
)