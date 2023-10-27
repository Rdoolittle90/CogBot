import datetime
import inspect
from nextcord import Interaction, slash_command
from nextcord.ext import commands
from src.extra.scripts.easy_modal import EasyModal

from src.bot import DiscordBot
from src.extra.scripts.colored_printing import colorized_print



class CoreCog(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.bot: DiscordBot = bot
        self.name = "Core"
        colorized_print("COG", "CoreCog connected")


    @slash_command(dm_permission=False, name="register", description=f"Core: Register with the bot to gain access to additional features.")
    async def register(self, interaction: Interaction):
        """
            Registers the users discord ID
        """
        colorized_print("COMMAND", f"{interaction.user.name} used {self.__cog_name__}.{inspect.currentframe().f_code.co_name} at {datetime.datetime.now()}")
        await interaction.response.send_modal(EasyModal(f"Register", self.register_callback, Steam_Friend_Code="optional"))


    async def register_callback(self, interaction: Interaction, entries):
        friend_code = None

        for item in entries:
            if item.label == "Steam_Friend_Code" and item.value != "optional":
                friend_code = item.value

        await  DiscordBot.sql.execute(
            "INSERT OR REPLACE INTO registrations (DUID, Handle, Avatar_URL, RegDate, SteamFC) VALUES (?, ?, ?, ?, ?)",
            interaction.user.id, 
            interaction.user.display_name, 
            interaction.user.avatar.url, 
            datetime.datetime.now(), 
            friend_code
        )
    

def setup(bot: DiscordBot):
    # bot.global_task_list.append((colorized_print, "TASK", "Core cog task added"))
    bot.add_cog(CoreCog(bot))
