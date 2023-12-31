import discord
from discord.app_commands import CommandTree
import random
import config

'''
--------CHANGE LOGS---------
VERSION: 1.2
BUILD: 1.5.6
BUGFIXES:
 + Reach Command now defered
 + List_Of_Listeners.count changed to len(List_Of_Listeners)
 + Added check for if emoji matched chossen emoji in On_Raw_Reaction_Add()
 + Listener changed to grab the first person in the list rather then someone random
 + Remove Listener from list once listener is chossen
 + Sets permissions of room to not include @verified
 + Defered /done command
FEATURE CHANGES:
 + Added Reaction Roles
 + Added Reaction Roles Embeds
CONFIG.PY CHANGES:
 + Added Reaction Role Guild Spesific Variables
 
Author - @moss1134
Discord - Marcia1134
Telegram - @Mossmarcia1134

Please contact me with any bugs or questions.
'''

# Discord API Set-up
intents = discord.Intents.all()
discord_client = discord.Client(intents=intents)
tree = CommandTree(discord_client)
discord_client.tree = tree

# Globals
list_of_listeners = []
# global age emoji's
age_emojis = ["🌻", "🌺", "🌸", "🌷", "💐", "☘", "🌵", "🎋", "🌲"]
dm_status_emojis = ["🔓", "🔐", "🔒"]
timezone_emojis = ["🌑", "🌘", "🌗", "🌖", "🌕", "🌔", "🌓", "🌒"]
# Colour Variables
wisteria_c = 0xcba3e8

@discord_client.event
async def on_ready():
    synced = await discord_client.tree.sync()
    print(str(len(synced)) + " commands have been loaded and are ready for use!")

# All commands to do with OTU embeds:

# Hard coded embeds

@discord_client.tree.command(name="print_welcome_embed", description="Prints a given embed", nsfw="false")
async def print_welcome_embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Welcome to Discord Heal Hub!", color=0xcba3e8)
    embed.add_field(name="What is DHH?", value="We are a safe-haven that attempts to support those who need it in a simple and easy way!", inline="true")
    embed.add_field(name="What is a member?", value="A member is someone that reaches out to a listener for support", inline="true")
    embed.add_field(name="What is a listener?", value="A listener is someone that has signed up to be there for others", inline="true")
    await interaction.channel.send(embed=embed)
    
@discord_client.tree.command(name="print_rules_embed", description="Prints the rules embed (Hardcoded)")
async def print_rules_embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Rules!", color=0xcba3e8)
    embed.add_field(name="Safe For All", value="This is a Safe Server for all kinds of problems. It is important never to judge anyone for the expirences they have made, or how they choose to identify, etc. DHH is a safe space for all people looking to vent or destress.", inline=False)
    embed.add_field(name="Be Nice!", value="Be respectful of others and understand some people in the server are not in the best state of mind. Be kind, understanding, and caring towards others!", inline=False)
    embed.add_field(name="Triggers", value="Please be mindful of tiggering topics when talking to other server members! Your triggers are expected to be in your introduction. If your triggers change you may go back and edit those introductions.", inline=False)
    embed.add_field(name="Language", value="We only support English in this server currently for effective moderation. Your use of language should be SFW (safe for work) and respectful. NO SLURS, NSFW LANGUAGE, ETC", inline=False)
    embed.add_field(name="Disclaimer", value="Please be aware that these rules will be used to judge whether message sent in the server are up to standard. These rules are not rock solid and will be effective on a case by case basis. If we find that you have clearly broken a rule for a reason that is not well- reasonable, moderators, admins and other rule enforces will act in the way they see fit. Please be respectful that moderators are here to mod, not members, if you are a member and see something, please report it rather then attempt to mod the situation. Thank you for understanding.", inline= False)
    await interaction.channel.send(embed=embed)

@discord_client.tree.command(name="print_reaction_roles_age", description="Prints the embed for reaction roles!")
async def print_reaction_roles_age(interaction: discord.Interaction):
    embed = discord.Embed(title="Age Reaction Roles!", colour=wisteria_c)
    embed.add_field(name="13 - 🌻", value="|--", inline=True)
    embed.add_field(name="14 - 🌺", value="|--", inline=True)
    embed.add_field(name="15 - 🌸", value="|--", inline=True)
    embed.add_field(name="16 - 🌷", value="|--", inline=True)
    embed.add_field(name="17 - 💐", value="|--", inline=True)
    embed.add_field(name="18 - ☘", value="|--", inline=True)
    embed.add_field(name="19 - 🌵", value="|--", inline=True)
    embed.add_field(name="20 - 🎋", value="|--", inline=True)
    embed.add_field(name="20+ - 🌲", value="|--", inline=True)
    embed.add_field(name="Remove all roles - 🚫", value="|--", inline=False)
    message = await interaction.channel.send(embed=embed)
    await message.add_reaction(str(age_emojis[0]))
    await message.add_reaction(str(age_emojis[1]))
    await message.add_reaction(str(age_emojis[2]))
    await message.add_reaction(str(age_emojis[3]))
    await message.add_reaction(str(age_emojis[4]))
    await message.add_reaction(str(age_emojis[5]))
    await message.add_reaction(str(age_emojis[6]))
    await message.add_reaction(str(age_emojis[7]))
    await message.add_reaction(str(age_emojis[8]))
    await message.add_reaction(str("🚫"))
    
@discord_client.tree.command(name="print_reaction_roles_dm_status", description="prints the reaction roles embed!")
async def print_reaction_roles_dm_status(interaction: discord.Interaction):
    embed = discord.Embed(title="DM Status Reaction Roles!", color=wisteria_c)
    embed.add_field(name=f"DMs open - {dm_status_emojis[0]}", value="|--", inline=True)
    embed.add_field(name=f"Ask for DMs - {dm_status_emojis[1]}", value="|--", inline=True)
    embed.add_field(name=f"DMs closed - {dm_status_emojis[2]}", value="|--", inline=True)
    embed.add_field(name="Remove all roles - 🚫", value="|--", inline=False)
    message = await interaction.channel.send(embed=embed)
    for x in dm_status_emojis:
        await message.add_reaction(str(x))
    await message.add_reaction(str("🚫"))

# custom embeds

@discord_client.tree.command(name="custom3_embed", description="Allows you to print a custom embed with 3 fields")
async def custom3_embed(interaction: discord.Interaction, inline: bool, title: str, color: int, name1: str, value1: str, name2: str, value2: str, name3: str, value3: str):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name1, value=value1, inline=inline)
    embed.add_field(name=name2, value=value2, inline=inline)
    embed.add_field(name=name3, value=value3, inline=inline)
    await interaction.channel.send(embed=embed)
    
@discord_client.tree.command(name="custom2_embed", description="Allows you to print a custom embed with 2 fields")
async def custom2_embed(interaction: discord.Interaction, inline: bool, title: str, color: int, name1: str, value1: str, name2: str, value2: str):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name1, value=value1, inline=inline)
    embed.add_field(name=name2, value=value2, inline=inline)
    await interaction.channel.send(embed=embed)
    
@discord_client.tree.command(name="custom1_embed", description="Allows you to print a custom embed with 1 field")
async def custom2_embed(interaction: discord.Interaction, inline: bool, title: str, color: int, name1: str, value1: str):
    embed = discord.Embed(title=title, color=color)
    embed.add_field(name=name1, value=value1, inline=inline)
    await interaction.channel.send(embed=embed)

# All Multi-Use Embeds

@discord_client.tree.command(name="help", description="Help command")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", color=0xcba3e8, url="https://github.com/Moss1134/MentalHealthDiscordApp/wiki")
    embed.add_field(name="Where can I go to understand the discord bot commands?", value="You can head to the Work In Progress Github Wiki", inline=False)
    await interaction.response.send_message(embed=embed)

# verification system

@discord_client.event
async def on_message(message):
    if message.channel.id == config.guild_veify_channel_id: # Checks if message was coming from the #Verify Text channel
        if message.author != discord_client.user: # Checks if the message was by the python bot
            if message.content != "I pledge to follow all rules of DHH, be respectful and understanding towards all users.":
                await message.reply("Please read the Embed above!")
                await message.delete()
            else:
                await message.reply("Thank you for verifying! You will now be added as a server user!")
                await message.delete()
                await message.author.add_roles(message.guild.get_role(int(config.guild_veified_role_id))) # adds the role "Verified" to the user
        # deletes the bots response after 3 seconds
        if message.content == "Please read the Embed above!":
            await message.delete(delay=3)
        if message.content == "Thank you for verifying! You will now be added as a server user!":
            await message.delete(delay=3)

# reaction roles

@discord_client.event
async def on_raw_reaction_add(payload):
    emoji = "👍"
    emoji_remove = "🚫"
    emoji_str = str(payload.emoji)
    guild = discord_client.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)
    if payload.message_id == config.verify_message_id and emoji_str == emoji:
        await user.add_roles(guild.get_role(int(config.guild_veified_role_id)))
    elif payload.message_id == config.reaction_role_age_message_id and emoji_str in str(age_emojis):
        await user.add_roles(guild.get_role(int(config.age_roles_id[age_emojis.index(emoji_str)])))
    elif payload.message_id == config.reaction_role_age_message_id and emoji_str == str(emoji_remove):
        for x in config.age_roles_id:
            print(x)
            await user.remove_roles(guild.get_role(x))
    elif payload.message_id == config.reaction_role_dm_status_message_id and emoji_str in str(dm_status_emojis):
        await user.add_roles(guild.get_role(int(config.dm_status_roles_id[dm_status_emojis.index(emoji_str)])))
    elif payload.message_id == config.reaction_role_dm_status_message_id and emoji_str == str(emoji_remove):
        for x in config.dm_status_roles_id:
            await user.remove_roles(guild.get_role(x))

# Introduction system:

@discord_client.tree.command(name="introduce", description="creates an introduction for you!")
async def introduce(interaction: discord.Interaction, name: str, age: int, pronouns: str, region: str, triggers: str, hobbies: str, other: str):
    await interaction.response.send_message(f"- --**@{str(interaction.user)}**-- \n - My name is: **{name}** \n - I am **{str(age)}** years old! \n - I use **{pronouns}** \n - I live in: **{region}** \n - When talking to me please refrain from: **{triggers}** \n - I enjoy: **{hobbies}** \n - And a little note about me: \n **{other}**")

# Listener and Member role System

# Listening queue join

@discord_client.tree.command(name="listening", description="Adds to the list of people waiting to listen to other members")
async def listening(interaction: discord.Interaction):
    global list_of_listeners
    if str(interaction.user) not in list_of_listeners:
        list_of_listeners.append(str(interaction.user))
        await interaction.response.send_message(f"Thank you for adding yourself to the Listener list! You will be connected to a Member as soon as someone requests a Listener!")
    else:
        await interaction.response.send_message("You are already a part of the listener list, just hang on until someone requests a Listener. You can remove yourself from the list by using the `/leave` command")

# Listening queue leave

@discord_client.tree.command(name="leave")
async def leave(interaction: discord.Interaction):
    global list_of_listeners
    if str(interaction.user) in list_of_listeners:
        list_of_listeners.remove(str(interaction.user))
        await interaction.response.send_message("You have been removed from the Listner list")
    else:
        await interaction.response.send_message("You are not a part of the Listner list, if you would like to add yourself to the list; use the /listening command.")

# memeber connects with listener

@discord_client.tree.command(name="reach", description="Reaches out to a random Active Listener")
async def reach(interaction: discord.Interaction):
    global list_of_listeners
    if len(list_of_listeners) == 0:
        await interaction.response.send_message("Sorry, there are no current listeners avaliable, please wait 10 minutes and try again.")
    else:
        await interaction.response.defer()
        # Variables
        category = discord.utils.get(interaction.guild.categories, id=config.guild_room_category_id)
        listener = list_of_listeners[0]
        list_of_listeners.remove(listener)
        listener = interaction.guild.get_member_named(listener)
        num_of_chatrooms = len(category.channels)
        everyone_role = discord.utils.get(interaction.guild.roles, id=config.guild_global_role_id)
        verified_role = discord.utils.get(interaction.guild.roles, id=config.verified_role_id)
        # Create a channel:
        channel = await category.create_text_channel(name=f"chatroom-{str(num_of_chatrooms)}")
        # Sets the permssions for @everyone:
        perms = discord.PermissionOverwrite(view_channel=False)
        await channel.set_permissions(everyone_role, overwrite=perms)
        await channel.set_permissions(verified_role, overwrite=perms)
        # Create room role:
        room_role = await interaction.guild.create_role(name=f"room " + str(num_of_chatrooms))
        room_role = discord.utils.get(interaction.guild.roles, id=room_role.id)
        # Overwrite permissions for room_role:
        perms = discord.PermissionOverwrite(view_channel=True, send_messages=True)
        await channel.set_permissions(room_role, overwrite=perms)
        # Give everyone roles:
        await listener.add_roles(room_role)
        await interaction.user.add_roles(room_role)
        await interaction.followup.send(f"You have been connected with a listener! Please join chatroom {str(num_of_chatrooms)}!")

# Deletes role and channel after member/listener is fininhed with the chat.

@discord_client.tree.command(name="done", description="Closes a room once you are done talking")
async def done(interaction: discord.Interaction):
    category = discord.utils.get(interaction.guild.categories, id=config.guild_room_category_id)
    list_of_removable_channels = [channel.name for channel in category.channels]
    if interaction.channel.name in list_of_removable_channels:
        await interaction.response.defer()
        # Gets the room number for the room in question
        num: int = interaction.channel.name.strip("chatroom-")
        # Delete role
        await discord.utils.get(interaction.guild.roles, name=f"room " + str(num)).delete()
        # Delete channel
        await interaction.channel.delete()
    else:
        # Sends response if this command is used outside of the guild_room_category_id category
        await interaction.followup.send("You are trying to delete a channel outside of the CHATROOMS catergoy, please use the delete command or delete this channel mannually.")
    
discord_client.run(config.discord_application_token)
