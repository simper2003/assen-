import asyncio
import discord
import os
import json
import aiofiles
 

from discord import guild
from discord.ext import commands
from keep_alive import keep_alive
from discord_slash import SlashCommand , SlashCommandOptionType , SlashContext 
from discord_slash.utils.manage_commands import create_choice , create_option
from discord.ext.commands import has_permissions, MissingPermissions


#definds your Client

#definds your discord prefix

bot = discord.Client()


bot = commands.Bot(command_prefix=">", help_command=None, intents = discord.Intents().all())



slash = SlashCommand(bot, sync_commands=True)

format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

emojis = ["👍", "👎", "🗑️"]

@bot.event
async def on_ready():
    print("Your bot is ready.")


@bot.event
async def on_member_join(member):

	embed = discord.Embed(title=f"{member.guild.name}", description=f"**Welkom** {member.mention} in **{member.guild.name}**\nHopelijk heb je een leuke tijd hier, je bent het **{member.guild.member_count}**e lid!", color = 0x7289da)
	embed.set_thumbnail(url = f"{member.avatar_url}")
	embed.set_footer(text="Assen roleplay")
	await bot.get_channel(793963817087795271).send(embed=embed)



	


@bot.command(description = 'Add a suggestion for this community!')
async def suggest(ctx, desc=None, rep=None):
	user = ctx.author
	await ctx.channel.purge(limit = 1)
	await ctx.author.send("Wat is je suggestie? ")
	responseDesc = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=300)
	description = responseDesc.content
	await ctx.author.send("Je suggestie is verzonden.")
	embed = discord.Embed(title="Suggestie", description=description, color=0xffff)
	embed.set_author(name=f' {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
	embed.set_footer(text="Type >suggest voor een suggestie")
	SuggestChannel = bot.get_channel(793963450900414534)
	message = await SuggestChannel.send(embed=embed)
	for emoji in emojis:
            await message.add_reaction(emoji)


#groups de command
@bot.group()
async def info(ctx):
	await ctx.send("Probeer alle categorieën!:`>info`: *server*, *help*, *groepen*")

async def get_help_embed():
  em = discord.Embed(title="Assen roleplay", description="Hier kan je alles vinden wat je moet weten!")
  em.set_author(name="Bot Help")
  em.add_field(name="Over de bot", value="```-dit is een custom bot voor Assen roleplay!\n-met deze bot kan je commands vinden over de server over de groepen en meer!```", inline=False)
  em.add_field(name="Category's", value="```>info server, groepen, help | >fanart, >suggest```", inline=False)

  em.add_field(name="Setups(mod only)", value="```>info ticket, >info reactrole```")
  em.set_footer(text="Assen roleplay")
  return em

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        em = await get_help_embed()
        await message.channel.send(embed=em)

    await bot.process_commands(message)

@info.command()
async def help(ctx):
    em = await get_help_embed()
    await ctx.send(embed=em)




@info.command(name="server")
async def serverinfo(ctx):
	name = str(ctx.guild.name)
	description = str(ctx.guild.description)

	owner = str(ctx.guild.owner)
	roles = str(ctx.guild.roles)
	id = str(ctx.guild.id)
	region = str(ctx.guild.region)
	memberCount = str(ctx.guild.member_count)
	text_channels = len(ctx.guild.text_channels)
	icon = str(ctx.guild.icon_url)

	embed = discord.Embed(
		title=name + " Server Information",
		description=description,
		color=discord.Color.blue()
	)
	embed.set_thumbnail(url=icon)
	embed.add_field(name="Owner", value=owner, inline=False)
	embed.add_field(name="Description", value=description)
	embed.add_field(name="Region", value=region, inline=False)
	embed.add_field(name="Channels", value=text_channels)
	embed.add_field(name="Member Count", value=memberCount, inline=False)


	await ctx.send(embed=embed)

@bot.command(aliases=["em"])
async def embed(ctx):
	embed = discord.Embed(title="Ticket aan maken!", description="Maak een ticket aan om op de emoji te klikken!🎫", color=0x0000ff)
	embed.set_footer(text="Ticket Assen!")

	await ctx.send(embed=embed)




@info.command(name="groepen", aliases=["groups", "infog", "g"])
async def info_groepen(ctx):

	emb = discord.Embed(title="informatie Groepen", description="**Bekijk hier alle groepen!**", color=0x0000ff)
	emb.add_field(name="🚓Politie:", value="[Politie groep](https://www.roblox.com/groups/10187611/Nationale-Politie-Assen#!/about)", inline=False)
	emb.add_field(name="🚒Brandweer:", value="[Brandweer groep](https://www.roblox.com/groups/10240068/Brandweer-Assen#!/about)", inline=False)
	emb.add_field(name="🚑Ambulance:", value="[Ambulance groep](https://www.roblox.com/groups/10241149/Ambulance-Assen#!/about)", inline=False)
	emb.add_field(name="🚙Diens Verkeers Politie:", value="[Diens Verkeers Politie groep](https://www.roblox.com/groups/10417758/Dienst-Verkeers-Politie-Assen#!/about)", inline=False)
	emb.add_field(name="🕵️Dienst Speciale Interventies:", value="[Dienst Speciale Interventies groep](https://www.roblox.com/groups/10187385/Dienst-Speciale-Interventies-Assen#!/about)", inline=False)
	emb.add_field(name="🛑Rijkswaterstaat:", value="[Rijkswaterstaat groep](https://www.roblox.com/groups/10417654/Rijkswaterstaat-Assen#!/about)", inline=False)
	emb.add_field(name="👮‍♂️Koninklijke Marechaussee:", value="[Koninklijke Marechaussee groep](https://www.roblox.com/groups/10240071/Koninklijke-Marechaussee-Assen#!/about)", inline=False)
	emb.add_field(name="👷‍♂️Gemeente:", value="[Gemeente groep](https://www.roblox.com/groups/10187339/Gemeente-Assen-Roleplay#!/affiliates)", inline=False)
	emb.set_footer(text="Assen Roleplay")

	await ctx.send(embed=emb)



		
@info.command(name="reactrole")
async def reactrolehelp(ctx):
	embed = discord.embed(title="Reactrole_setup")
	embed.add_field(name="`")

@bot.command()
async def reactrole(ctx, emoji, role: discord.Role,*,message):

	emb = discord.Embed(description=message)
	msg = await ctx.channel.send(embed=emb)
	await msg.add_reaction(emoji)

	with open("reactrole.json") as json_file:
		data = json.load(json_file)

		new_react_role = {
			'role_name':role.name,
			'role_id':role.id,
			'emoji':emoji,
			'message_id':msg.id
		}

		data.append(new_react_role)

	with open("reactrole.json", "w") as j:
		json.dump(data,j,indent=4)



@bot.event
async def on_raw_reaction_add(payload):

	if payload.member.bot:
		pass

	else:

		with open("reactrole.json") as react_file:

			data = json.load(react_file)
			for x in data:
				if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
					role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x['role_id'])

					await payload.member.add_roles(role)


bot.ticket_configs = {}

@bot.event
async def on_ready():
    async with aiofiles.open("ticket_configs.txt", mode="a") as temp:
        pass

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]

    print(f"{bot.user.name} is ready.")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.id != bot.user.id and str(payload.emoji) == u"\U0001F3AB":
        msg_id, channel_id, category_id = bot.ticket_configs[payload.guild_id]

        if payload.message_id == msg_id:
            guild = bot.get_guild(payload.guild_id)

            for category in guild.categories:
                if category.id == category_id:
                    break

            channel = guild.get_channel(channel_id)

            ticket_channel = await category.create_text_channel(f"ticket-{payload.member.display_name}", topic=f"Een ticket voor {payload.member.display_name}.", permission_synced=True)
            
            await ticket_channel.set_permissions(payload.member, read_messages=True, send_messages=True)

            message = await channel.fetch_message(msg_id)
            await message.remove_reaction(payload.emoji, payload.member)

            await ticket_channel.send(f"{payload.member.mention} Dankje voor het maken van een ticket, gebruik **'-sluit'** om je ticket te sluiten!")

            try:
                await bot.wait_for("message", check=lambda m: m.channel == ticket_channel and m.author == payload.member and m.content == "-sluit", timeout=3600)

            except asyncio.TimeoutError:
                await ticket_channel.delete()

            else:
                await ticket_channel.delete()

@bot.command()
@commands.has_permissions(manage_messages=True)
async def configure_ticket(ctx, msg: discord.Message=None, category: discord.CategoryChannel=None):
    if msg is None or category is None:
        await ctx.channel.send("Failed to configure the ticket as an argument was not given or was invalid.")
        return

    bot.ticket_configs[ctx.guild.id] = [msg.id, msg.channel.id, category.id] # this resets the configuration

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        data = await file.readlines()

    async with aiofiles.open("ticket_configs.txt", mode="w") as file:
        await file.write(f"{ctx.guild.id} {msg.id} {msg.channel.id} {category.id}\n")

        for line in data:
            if int(line.split(" ")[0]) != ctx.guild.id:
                await file.write(line)
                
    await msg.add_reaction(u"\U0001F3AB")
    await ctx.channel.send("met succes een ticket ge configureerd")


@info.command(name="ticket")
async def _tickethelp(ctx):
    with open("data.json") as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if ctx.author.guild_permissions.administrator or valid_user:

        em = discord.Embed(title="Assen tickets Help", description="", color=0x00a8ff)
        em.add_field(name="`>new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.", inline=False)
        em.add_field(name="`>close`", value="Use this to close a ticket. This command only works in ticket channels.")
        em.add_field(name="`>addaccess <role_id>`", value="This can be used to give a specific role access to all tickets. This command can only be run if you have an admin-level role for this bot.", inline=False)
        em.add_field(name="`>delaccess <role_id>`", value="This can be used to remove a specific role's access to all tickets. This command can only be run if you have an admin-level role for this bot.", inline=False)
        em.add_field(name="`>addpingedrole <role_id>`", value="This command adds a role to the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.", inline=False)
        em.add_field(name="`>delpingedrole <role_id>`", value="This command removes a role from the list of roles that are pinged when a new ticket is created. This command can only be run if you have an admin-level role for this bot.")
        em.add_field(name="`>addadminrole <role_id>`", value="This command gives all users with a specific role access to the admin-level commands for the bot, such as `>addpingedrole` and `>addaccess`. This command can only be run by users who have administrator permissions for the entire server.", inline=False)
        em.add_field(name="`>deladminrole <role_id>`", value="This command removes access for all users with the specified role to the admin-level commands for the bot, such as `>addpingedrole` and `>addaccess`. This command can only be run by users who have administrator permissions for the entire server.", inline=False)
        em.set_footer(text="Assen tickets")

        await ctx.send(embed=em)
    
    else:

        em = discord.Embed(title = "Assen tickets Help", description ="", color = 0x00a8ff)
        em.add_field(name="`>new <message>`", value="This creates a new ticket. Add any words after the command if you'd like to send a message when we initially create your ticket.")
        em.add_field(name="`>close`", value="Use this to close a ticket. This command only works in ticket channels.")
        em.set_footer(text="Assen tickets")

        await ctx.send(embed=em)

@bot.command()
async def new(ctx, *, args = None):

    await bot.wait_until_ready()

    if args == None:
        message_content = "Wacht even tot dat er een stafflid naar je toekomt"
    
    else:
        message_content = "".join(args)

    with open("data.json") as f:
        data = json.load(f)

    ticket_number = int(data["ticket-counter"])
    ticket_number += 1

    ticket_channel = await ctx.guild.create_text_channel("ticket-{}".format(ticket_number))
    await ticket_channel.set_permissions(ctx.guild.get_role(ctx.guild.id), send_messages=False, read_messages=False)

    for role_id in data["valid-roles"]:
        role = ctx.guild.get_role(role_id)

        await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
    
    await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

    em = discord.Embed(title="Een nieuwe ticket van {}#{}".format(ctx.author.name, ctx.author.discriminator), description= "{}".format(message_content), color=0x00a8ff)

    await ticket_channel.send(embed=em)

    pinged_msg_content = ""
    non_mentionable_roles = []

    if data["pinged-roles"] != []:

        for role_id in data["pinged-roles"]:
            role = ctx.guild.get_role(role_id)

            pinged_msg_content += role.mention
            pinged_msg_content += " "

            if role.mentionable:
                pass
            else:
                await role.edit(mentionable=True)
                non_mentionable_roles.append(role)
        
        await ticket_channel.send(pinged_msg_content)

        for role in non_mentionable_roles:
            await role.edit(mentionable=False)
    
    data["ticket-channel-ids"].append(ticket_channel.id)

    data["ticket-counter"] = int(ticket_number)
    with open("data.json", 'w') as f:
        json.dump(data, f)
    
    created_em = discord.Embed(title="Assen tickets", description="Je hebt een ticket aangemaakt in {}".format(ticket_channel.mention), color=0x00a8ff)
    
    await ctx.send(embed=created_em)

@bot.command()
async def close(ctx):
    with open('data.json') as f:
        data = json.load(f)

    if ctx.channel.id in data["ticket-channel-ids"]:

        channel_id = ctx.channel.id

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "close"

        try:

            em = discord.Embed(title="Assen tickets", description="Weet je zeker dat je de ticket wilt sluiten? typ `close` Als je het zeker weet", color=0x00a8ff)
        
            await ctx.send(embed=em)
            await bot.wait_for('message', check=check, timeout=60)
            await ctx.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)
            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)
        
        except asyncio.TimeoutError:
            em = discord.Embed(title="Assen tickets", description="Je bent te laat om de ticket te sluiten, probeer de command opnieuw", color=0x00a8ff)
            await ctx.send(embed=em)

        

@bot.command()
async def addaccess(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:
        role_id = int(role_id)

        if role_id not in data["valid-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["valid-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)
                
                em = discord.Embed(title="Assen tickets", description="Je hebt succesvol de role `{}` Tot de lijst die toegang heeft tot de tickets".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Assen tickets", description="Dat is geen geldige rol-ID. Probeer het opnieuw met een geldige rol-ID.")
                await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Assen tickets", description="Deze role heeft al toegang tot de tickets", color=0x00a8ff)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Assen tickets", description="Sorry je hebt geen permissie om deze command te runnen", color=0x00a8ff)
        await ctx.send(embed=em)

@bot.command()
async def delaccess(ctx, role_id=None):
    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass

    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            valid_roles = data["valid-roles"]

            if role_id in valid_roles:
                index = valid_roles.index(role_id)

                del valid_roles[index]

                data["valid-roles"] = valid_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Assen tickets", description="Je hebt met succes de role `{}` Van de lijst gehaald die geen toegang heeft tot de tickets".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)
            
            else:
                
                em = discord.Embed(title="Assen tickets", description="Deze role heeft al geen toegang tot de tickets", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Assen tickets", description="Dat is geen geldige role-ID Probeer het opnieuw met een geldige role-ID.")
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Assen tickets", description="Sorry, je hebt geen permissie om deze command te runne", color=0x00a8ff)
        await ctx.send(embed=em)

@bot.command()
async def addpingedrole(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        role_id = int(role_id)

        if role_id not in data["pinged-roles"]:

            try:
                role = ctx.guild.get_role(role_id)

                with open("data.json") as f:
                    data = json.load(f)

                data["pinged-roles"].append(role_id)

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Assen tickets", description="Je hebt met succes de role `{}` naar de lijst die worden gepinged als er een ticket word gemaakt".format(role.name), color=0x00a8ff)

                await ctx.send(embed=em)

            except:
                em = discord.Embed(title="Assen tickets", description="Dat is geen geldige role-ID Probeer het opnieuw met een geldige role-ID.")
                await ctx.send(embed=em)
            
        else:
            em = discord.Embed(title="Assen tickets", description="Deze role krijgt al een pinjg als er een ticket word aangemaakt", color=0x00a8ff)
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Assen tickets", description="Sorry, je hebt geen permissie om deze command te runne", color=0x00a8ff)
        await ctx.send(embed=em)

@bot.command()
async def delpingedrole(ctx, role_id=None):

    with open('data.json') as f:
        data = json.load(f)
    
    valid_user = False

    for role_id in data["verified-roles"]:
        try:
            if ctx.guild.get_role(role_id) in ctx.author.roles:
                valid_user = True
        except:
            pass
    
    if valid_user or ctx.author.guild_permissions.administrator:

        try:
            role_id = int(role_id)
            role = ctx.guild.get_role(role_id)

            with open("data.json") as f:
                data = json.load(f)

            pinged_roles = data["pinged-roles"]

            if role_id in pinged_roles:
                index = pinged_roles.index(role_id)

                del pinged_roles[index]

                data["pinged-roles"] = pinged_roles

                with open('data.json', 'w') as f:
                    json.dump(data, f)

                em = discord.Embed(title="Assen tickets", description="Je hebt met succes de role `{}` Van de lijst gehaald die worden gepinged waneer er een ticket word gemaakt.".format(role.name), color=0x00a8ff)
                await ctx.send(embed=em)
            
            else:
                em = discord.Embed(title="Assen tickets", description="Deze role word al niet gepinged waneer er een ticket word gemaakt.", color=0x00a8ff)
                await ctx.send(embed=em)

        except:
            em = discord.Embed(title="Assen tickets", description="Dat is geen geldige role-ID Probeer het opnieuw met een geldige role-ID.")
            await ctx.send(embed=em)
    
    else:
        em = discord.Embed(title="Assen tickets", description="Sorry, je hebt geen permissie om deze command te runne", color=0x00a8ff)
        await ctx.send(embed=em)


@bot.command()
@has_permissions(administrator=True)
async def addadminrole(ctx, role_id=None):

    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        data["verified-roles"].append(role_id)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        em = discord.Embed(title="Assen tickets", description="Je hebt met succes de role `{}` Tot de lijst die de admin-level commands.".format(role.name), color=0x00a8ff)
        await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Assen tickets", description="Dat is geen geldige role-ID Probeer het opnieuw met een geldige role-ID.")
        await ctx.send(embed=em)

@bot.command()
@has_permissions(administrator=True)
async def deladminrole(ctx, role_id=None):
    try:
        role_id = int(role_id)
        role = ctx.guild.get_role(role_id)

        with open("data.json") as f:
            data = json.load(f)

        admin_roles = data["verified-roles"]

        if role_id in admin_roles:
            index = admin_roles.index(role_id)

            del admin_roles[index]

            data["verified-roles"] = admin_roles

            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            em = discord.Embed(title="Assen tickets", description="Je hebt met succes de role `{}` Van de lijst gehaald die worden gepingen waneer er een ticket word aangemaakt".format(role.name), color=0x00a8ff)

            await ctx.send(embed=em)
        
        else:
            em = discord.Embed(title="Assen tickets", description="Deze role word niet gepinged waneer er een ticket word aangemaakt", color=0x00a8ff)
            await ctx.send(embed=em)

    except:
        em = discord.Embed(title="Assen tickets", description="Dat is geen geldige role-ID Probeer het opnieuw met een geldige role-ID.")
        await ctx.send(embed=em)







@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print("----------------------------------------")
 
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"@Assen! | >info help"))
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}')
                print(f'[ERROR] {e}')

    print("----------------------------------------")








keep_alive()
bot.run("")


