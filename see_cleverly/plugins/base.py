from dataclasses import dataclass
from psycopg_pool.pool_async import AsyncConnectionPool
from enum import StrEnum


@dataclass
class Repository:
    pool: AsyncConnectionPool


class Status(StrEnum):
    yes = "yes"
    no = "no"
