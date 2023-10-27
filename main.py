from dotenv import load_dotenv
from os import getenv

from src.bot import DiscordBot

load_dotenv()


def main():
    bot = DiscordBot()
    bot.run(getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()
