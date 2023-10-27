# CogBot: A Modular Discord Bot

CogBot is a Discord bot project built using the `nextcord` library, designed with modularity in mind. By utilizing "Cogs", users can easily extend the bot's functionality, turning on and off features as required, and even add their own.

## Main Features:

### 1. **Modularity with Cogs:**

- Cogs are akin to plugins or modules for the bot. They contain a specific set of features or commands that can be easily loaded or unloaded.
  
- To add new functionality to CogBot, simply drop a cog into the `src/cogs` directory. CogBot will recognize and load it.

### 2. **Pre-configured Paths:**

- CogBot knows exactly where to look for cogs, scripts, fonts, and other necessary files. The paths are already set up in the script, ensuring a smooth and easy setup.

### 3. **Database Integration with SQLite:**

- CogBot uses the `SQLManager` class for its interactions with an SQLite database, making it simpler to manage server settings or any other data you might want to store.

### 4. **Customizable Title and Versioning:**

- Fetch the bot's name and version from environment variables, allowing for easy branding and version control.

### 5. **Event Listeners:**

- CogBot is prepared to listen to various Discord events such as message sending, member joining, and more. Customize these as you see fit to create a responsive and interactive bot.

### 6. **Task Loops:**

- Keep the bot active and responsive with loops that can run tasks globally or specific to individual guilds.

## Getting Started:

1. **Setup:** Clone or download the CogBot repository.

2. **Environment Variables:** Set up the following environment variables:

   - **APP_VERSION:** Version of the bot.
   - **APP_NAME:** Name of the bot.
   - **APP_LOGGING_LEVEL** Debug level of the bot
   - **DISCORD_TOKEN** Your bots token
   - **OPEN_AI_TOKEN** Your OpenAI API token
   - **IMGUR_CLIENT_ID** Your Imgur client ID
   - **IMGUR_CLIENT_SECRET** Your Imgur client Secret

3. **Adding Cogs:** Navigate to the `src/cogs` directory and drop any cogs you want to include. The bot will automatically load them on startup.

4. **Dependencies:** Ensure all dependencies are installed via `pip`. Note that as of now, some cogs might require additional dependencies which you'll need to install manually. Future updates aim to automate this process.

## Dependencies:
`pip install -r requirements.txt` will install the following packages
- aiohttp>=3.8.6
- aiosignal>=1.3.1
- aiosqlite>=0.19.0
- async-timeout>=4.0.3
- attrs>=23.1.0
- certifi>=2023.7.22
- charset-normalizer>=3.3.1
- colorama>=0.4.6
- frozenlist>=1.4.0
- idna>=3.4
- imgurpython>=1.1.7
- multidict>=6.0.4
- nextcord>=2.6.0
- openai>=0.28.1
- python-dotenv>=1.0.0
- requests>=2.31.0
- tqdm>=4.66.1
- typing_extensions>=4.8.0
- urllib3>=2.0.7
- yarl>=1.9.2


## Conclusion:

CogBot aims to provide a seamless and modular experience for Discord bot development. With the flexibility of cogs, you can make your bot as minimal or feature-rich as you desire. Dive in and start customizing your CogBot today!
