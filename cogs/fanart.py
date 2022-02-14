import discord
from discord.ext import commands
import asyncio

emojis = ["👍"]


class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bug(self, ctx, desc=None, rep=None):
        await ctx.channel.purge(limit=1)
        user = ctx.author
        await ctx.author.send('```Beschrijf je fanart hier | bijv *het is een auto* ```')
        responseDesc = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
        description = responseDesc.content
        await ctx.author.send('```Geef je foto van je fanart zodat ik die kan plaatsen :)```')
        responseRep = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
        replicate = responseRep.content
        await ctx.author.send('Je fanart is verzonden :)')
        embed = discord.Embed(title='Bug Report', color=0x00ff00)
        embed.add_field(name='Description',
                        value=description, inline=False)
        embed.add_field(name='Replicate', value=replicate, inline=True)
        embed.add_field(name='Reported By', value=user, inline=True)
        adminBug = self.bot.get_channel(846484499897778267)
        message = await adminBug.send(embed=embed)
        for emoji in emojis:
            await message.add_reaction(emoji)






def setup(bot):
    bot.add_cog(Bug(bot))