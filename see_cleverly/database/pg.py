from psycopg_pool.pool_async import AsyncConnectionPool
from functools import lru_cache
import os
import asyncio


# async lru_caching
def async_lru_cache(*lru_cache_args, **lru_cache_kwargs):
    def async_lru_cache_decorator(async_function):
        @lru_cache(*lru_cache_args, **lru_cache_kwargs)
        def cached_async_function(*args, **kwargs):
            coroutine = async_function(*args, **kwargs)
            return asyncio.ensure_future(coroutine)

        return cached_async_function

    return async_lru_cache_decorator


@async_lru_cache()
async def get_db():
    pool = AsyncConnectionPool(os.environ["DATABASE_CONNECTION_STRING"])
    await pool.open()
    return pool
