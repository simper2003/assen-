import discord
from discord.ext import commands

class training(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

		@commands.group(name="training")
		async def training(self, ctx, title=None, eenheid=None, type=None, tijd=None, datum=None, host=None, supervisor=None, opmerking=None):
			await ctx.send("wat is de title?")

		

# @bot.command()
#@commands.has_permissions(administrator=True)
#async def training(ctx, title=None, eenheid=None, type=None, tijd=None, datum=None, host=None, supervisor=None, opmerking=None):
#	await ctx.send("wat is de Title?")
#	responseTitle = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	title = responseTitle.content
#	await ctx.send("Wat is de eenheid waar mee je gaat trainen?")
#	responseEenheid = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	eenheid = responseEenheid.content
#	await ctx.send("Wat voor type training is het?")
#	responseTypen = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#typen = responseTypen.content
#	await ctx.send("Hoelaat word de training gehouden?")
#	responseTijd = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	tijd = responseTijd.content 
#	await ctx.send("wat is de datum van de training?")
#	responseDatum = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	datum = responseDatum.content 
#	await ctx.send("Wie word de host?")
#	responseHost = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	host = responseHost.content
#	await ctx.send("Wie word de supervisor?")
#	responseSupervisor = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	supervisor = responseSupervisor.content
#	await ctx.send("Heb je nog een opmerking voor de training? | de link van de game")
#	responseOpmerking = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
#	opmerking = responseOpmerking.content
#	embed = discord.Embed(title=title, color=0xffff)
#	embed.add_field(name="Eenheid", value=eenheid, inline=False)
#	embed.add_field(name="Type", value=typen, inline=False)
#	embed.add_field(name="Tijd", value=tijd, inline=False)
#	embed.add_field(name="Datum", value=datum, inline=False)
#	embed.add_field(name="Host", value=host, inline=False)
#	embed.add_field(name="Supervisor", value=supervisor, inline=False)
#	embed.add_field(name="Opmerking", value=opmerking, inline=False)
#	embed.set_footer(text="Assen roleplay training")
#	trainingChannel = bot.get_channel(825747801958514720)
#	message = await trainingChannel.send(embed=embed)

 

def setup(bot):
    bot.add_cog(training(bot))
