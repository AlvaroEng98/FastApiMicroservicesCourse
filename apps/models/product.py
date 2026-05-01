from redis_om import HashModel
from apps.core.redis_client import redis_conn

class Product(HashModel):

    name : str
    price : float
    quantity : int

    class Meta:
        database = redis_conn