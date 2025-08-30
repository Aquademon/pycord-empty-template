from discord.ext import commands
from src.utils.logger import setup_logger

class Ready(commands.Cog):
    def __init__(self, bot):
        self.logger = setup_logger(__name__)
        self.bot = bot
        self.bot.loop.create_task(self.send_status_message())

    async def log(self):
        await self.bot.wait_until_ready()
        self.logger.info(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')

def setup(bot):
    bot.add_cog(Ready(bot))
