import datetime
import aiosqlite

from src.extra.scripts.colored_printing import colorized_print



class SQLManager():
    db_path = "src/save/sql/core.db"
    templates = "src/save/sql/templates"

    async def ready_sql(self):
        async with aiosqlite.connect(SQLManager.db_path) as conn:
            with open(f"{SQLManager.templates}/default.sql", "r") as f:
                await conn.executescript(f.read())
            await conn.commit()

    async def execute(self, query, *args) -> tuple:
        async with aiosqlite.connect(SQLManager.db_path) as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(query, args)
                result = await cursor.fetchall()
            await conn.commit()

            colorized_print("DEBUG", f"The query {query} was executed successfully {datetime.datetime.now()}")
            if result != None:
                return result
            else:
                colorized_print("DEBUG", f"The query {query} was executed successfully with no results {datetime.datetime.now()}")

    async def executescript(self, file_path):
        async with aiosqlite.connect(SQLManager.db_path) as conn:
            with open(file_path, "r") as f:
                await conn.executescript(f.read())
            await conn.commit()
            colorized_print("DEBUG", f"The file @{file_path} was executed successfully {datetime.datetime.now()}")

