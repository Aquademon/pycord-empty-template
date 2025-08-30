import os
import discord
from dotenv import load_dotenv
from src.utils.logger import setup_logger

load_dotenv()

class Bot(discord.Bot):
    def __init__(self):
        self.logger = setup_logger(__name__)
        intents = discord.Intents.all()
        super().__init__(intents=intents)

    async def on_ready(self):

        await self.load_cogs()

    async def load_cogs(self):
        for root, _, files in os.walk("./src/cogs"):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    rel_path = os.path.relpath(os.path.join(root, file), ".")
                    extension = rel_path.replace(os.sep, ".")[:-3]
                    try:
                        self.load_extension(extension)
                        self.logger.info(f'Successfully loaded: {extension}')
                    except Exception as e:
                        self.logger.error(f'Failed to load {extension}: {str(e)}')

bot = Bot()
bot.run(os.getenv("DISCORD_TOKEN"))