from typing import Optional
from ...base import Repository, Status
from datetime import datetime, timezone, timedelta


class LightRepository(Repository):
    capture_interval: 60

    async def add(
        self,
        located_at: str,
        capture_interval: Optional[int] = None,
        camera_id: Optional[int] = None,
    ):
        async with self.pool.connection() as connection:
            async with connection.cursor() as cursor:
                if capture_interval is None:
                    capture_interval = self.capture_interval
                await cursor.execute(
                    "INSERT INTO \
                                     light (camera_id, located_at, capture_interval) \
                                     VALUES (?,?,?);",
                    (camera_id, located_at, capture_interval),
                )

    async def add_activity(
        self, captured_timestamp: datetime, light_id: int, switched_on: Status
    ):
        async with self.pool.connection() as connection:
            async with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO \
                        light_activity(captured_at, light_id, switched_on) \
                            VALUES (?,?,?)",
                    (
                        captured_timestamp.astimezone(timezone.utc),
                        light_id,
                        switched_on,
                    ),
                )

    async def get_number_of_lights_with_no_people(
        self, wait_until=timedelta(minutes=5)
    ):
        async with self.pool.connection() as connection:
            async with connection.cursor() as cursor:
                await cursor.execute(
                    " SELECT * \
                        FROM light_activity \
                            WHERE now() - captured_at < INTERVAL '? seconds' and switched_on='no'; \
                            ",
                    wait_until.total_seconds(),
                )
                return cursor.fetchall()
