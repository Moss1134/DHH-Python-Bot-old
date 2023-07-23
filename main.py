import discord
from discord.app_commands import CommandTree
import random
import config

# Discord API Set-up
intents = discord.Intents.all()
discord_client = discord.Client(intents=intents)
tree = CommandTree(discord_client)
discord_client.tree = tree

# Globals
list_of_listeners = []

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

# Commands to do with channels

@discord_client.tree.command(name="create_test_channel", description="Creates a test channel")
async def create_test_channel(interaction: discord.Interaction):
    await interaction.guild.create_text_channel(name="test", position=len(interaction.guild.channels) + 1)
    await interaction.response.send_message("Channel test has been created")

# verification system

@discord_client.event
async def on_message(message):
    if message.channel.id == config.guild_veify_channel_id: # Checks if message was coming from the #Verify Text channel
        if message.author != discord_client.user: # Checks if the message was by the python bot
            if message.content != "I am a user of the DHH and I will pledge to follow all rules. I am not currently affected by self-harm, or suicide, and I do not abuse anyone.":
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

# Debug Commands for Listening queue

@discord_client.tree.command(name="dev")
async def dev(interaction: discord.Interaction):
    await interaction.response.send_message(str(list_of_listeners))

@discord_client.tree.command(name="dev_add")
async def dev_add(interaction: discord.Interaction, name: str):
    global list_of_listeners
    list_of_listeners.append(name)
    await interaction.response.send_message("Added")    

@discord_client.tree.command(name="dev_set")
async def dev_add(interaction: discord.Interaction):
    global list_of_listeners
    list_of_listeners.append("hey1")
    list_of_listeners.append("hey2")
    list_of_listeners.append("hey3")
    list_of_listeners.append("hey4")
    list_of_listeners.append("hey5")
    list_of_listeners.append("hey6")
    await interaction.response.send_message("Added") 

# memeber connects with listener

@discord_client.tree.command(name="reach1", description="reaches out to a random listner")
async def reach1(interaction: discord.Interaction):
    global list_of_listeners
    listener = list_of_listeners[random.randint(0,len(list_of_listeners)-1)]
    await interaction.response.send_message("We will connect you with " + str(listener) + " \n This is a test message", ephemeral=True)
    # Find the category using its ID
    category_id = 1132460675957014548
    category = discord.utils.get(interaction.guild.categories, id=category_id)
    # Check if the category was found before creating the text channel
    if category is not None:
        num_of_channels = len(category.channels)
        channel = await category.create_text_channel(name="chat-room-" + str(num_of_channels))
    else:
        print(f"Category with ID {category_id} not found.")
    await channel.set_permissions(discord.utils.get(interaction.guild.roles, id=config.guild_global_role_id), view_channel=False)
    room_role = await interaction.guild.create_role(name=f"room " + str(num_of_channels))
    perms = discord.PermissionOverwrite(view_channel=True, send_messages=True)
    await channel.set_permissions(discord.utils.get(interaction.guild.roles, id=room_role.id), overwrite=perms)
    listener = interaction.guild.get_member_named(listener)
    await listener.add_roles(discord.utils.get(interaction.guild.roles, id=room_role.id))
    await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id=room_role.id))
    

    
@discord_client.tree.command(name="done", description="Closes a room once you are done talking")
async def done(interaction: discord.Interaction):
    await interaction.response.send_message("This is a incomplete command and nothing has run except sending this message.")
    
discord_client.run(config.discord_application_token)
