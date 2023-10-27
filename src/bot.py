import asyncio
import os
from nextcord import Intents, Member, Message
from nextcord.ext import commands, tasks
from src.save.sql.sql_manager import SQLManager

from src.extra.scripts.colored_printing import colorized_print
from src.extra.scripts.divider_title import divider_title



class DiscordBot(commands.Bot):
    intents:Intents = Intents.default()
    intents.message_content = True
    intents.members = True
    prefix = commands.when_mentioned

    paths = {
        "cogs": "src/cogs",
        "scripts": "src/extra/scripts",
        "fonts": "src/extra/fonts",
        "temp": "src/save/temp"
    }
    sql: SQLManager = SQLManager()

    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix=DiscordBot.prefix, intents=DiscordBot.intents, *args, **kwargs)
        self.name = os.getenv("APP_NAME")
        self.version = os.getenv("APP_VERSION")
        self.app_title = f"{self.name} v.{self.version}"
        self.width = len(self.app_title) + 32
        self.primary_symbol = "="
        self.secondary_symbol = "-"

        self.guild_task_list = []
        self.global_task_list = []

        self.cogs_loaded = False
        self.startup()

        self.ready = False
        


    def startup(self) -> None:
        self.display_title()
        
        divider_title("Connections", self.width, self.secondary_symbol)
        asyncio.run(DiscordBot.sql.ready_sql())
        colorized_print("CONN", "sql/save/sql/core.db")


        self.add_listener(self.on_member_join)
        self.add_listener(self.on_member_remove)
        self.add_listener(self.on_message)
        self.add_listener(self.on_ready)
        
        self.load_cogs()
        divider_title("Output", self.width, self.secondary_symbol)


    async def on_message(self, message: Message) -> None:
        """
        Event handler for the `on_message` event.

        This method is called when a message is sent in a server where the bot is present. 
        It checks the message for any attachments and saves them to disk.

        Args:
            message (Message): The message object containing the message content and attachments.

        Returns:
            (None)

        """
        pass


    async def on_member_join(self, member: Member) -> None:
        """
        Event handler for the `on_member_join` event.

        This method is called when a new member joins the server. It logs the event to the console.

        Args:
            member (nextcord.Member): The member object representing the new member.

        Returns:
            (None)

        """
        print(member.display_name)


    async def on_member_remove(self, member: Member) -> None:
        """
        Event handler for the `on_member_remove` event.

        This method is called when a member leaves the server. It logs the event to the console.

        Args:
            member (nextcord.Member): The member object representing the departing member.

        Returns:
            (None)

        """
        pass


    async def on_ready(self) -> None:
        if self.ready:
            pass

        if not self.global_update.is_running():
            self.global_update.start()
        if not self.guild_update.is_running():
            self.guild_update.start()
        
        # for guild in self.guilds:
        #     await DiscordBot.sql.execute(
        #         "INSERT OR IGNORE INTO settings (GuildID, AdminEnabled, DebugEnabled) VALUES (?, ?, ?);",
        #         guild.id, 0, 0
        #     )
        
        self.ready = True


    def display_title(self):
        print()
        divider_title("", self.width, self.primary_symbol)
        divider_title(self.app_title, self.width, " ")
        divider_title("", self.width, self.primary_symbol)


    def load_cogs(self):
        if self.cogs_loaded:
            return

        divider_title("Cogs", self.width, self.secondary_symbol)
        all_extension_folders = [i for i in os.listdir("src/cogs") if os.path.isdir(os.path.join("src/cogs", i))]
        for folder in all_extension_folders:
            cogs = [i.removesuffix(".py") for i in os.listdir(f"src/cogs/{folder}") if i.endswith(".py") and i != "__init__.py"]
            for extension in cogs:
                self.load_extension(f"src.cogs.{folder}.{extension}")

        self.cogs_loaded = True



    @tasks.loop(seconds=1)
    async def global_update(self):
        if len(self.global_task_list) > 0:
            for task in self.global_task_list.copy():
                try:
                    func, *args = task
                    
                    if asyncio.iscoroutinefunction(func):
                        await func(*args)
                    else:
                        func(*args)
                except Exception as e:
                    print(f"An error occurred while running the task: {str(e)}")
        else:
            colorized_print("DEBUG", "No global tasks in task list")
            self.global_update.stop()

    @global_update.before_loop
    async def before_update(self):
        colorized_print("DEBUG", 'Waiting until bot is ready to start global_update loop')
        await self.wait_until_ready()


    @tasks.loop(seconds=10)  # Set the interval here
    async def guild_update(self):
        if len(self.guild_task_list) > 0:
            for task in self.guild_task_list:
                for _ in self.guilds:
                    await task[0](*task[1:])
        else:
            colorized_print("DEBUG", "No guild tasks in task list")
            self.guild_update.stop()

    @guild_update.before_loop
    async def before_update(self):
        colorized_print("DEBUG", 'Waiting until bot is ready to start guild_update loop')
        await self.wait_until_ready()



    async def get_settings(self, guildID, table_name="settings"):
        result = await DiscordBot.sql.execute(
            f"SELECT * FROM {table_name} WHERE GuildID = ?;",
            guildID
        )
        return result[0]
