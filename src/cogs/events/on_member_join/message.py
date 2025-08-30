# src/cogs/events/member_events.py
import discord
from discord.ext import commands
from datetime import datetime


class MemberEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Event: When a member joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} joined {member.guild.name}")

        welcome_channel = discord.utils.get(member.guild.channels, name="welcome")
        if welcome_channel:
            embed = discord.Embed(
                title="Welcome!",
                description=f"Welcome to {member.guild.name}, {member.mention}!",
                color=discord.Color.green(),
                timestamp=datetime.now()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.add_field(
                name="Member Count",
                value=f"You are member #{member.guild.member_count}!",
                inline=False
            )
            await welcome_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MemberEventsCog(bot))