import discord
from discord.app_commands import CommandTree
import config

intents = discord.Intents.all()
discord_client = discord.Client(intents=intents)
tree = CommandTree(discord_client)
discord_client.tree = tree

@discord_client.event

async def on_ready():
    synced = await discord_client.tree.sync()
    print(str(len(synced)) + " have been loaded and are ready for use!")

# All commands to do with OTU embeds:

# Hard coded embeds

@discord_client.tree.command(name="print_welcome_embed", description="Prints a given embed", nsfw="false")
async def print_welcome_embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Welcome to Discord Heal Hub!", color=0xcba3e8)
    embed.add_field(name="What is DHH?", value="We are a safe-haven that attempts to support those who need it in a simple and easy way!", inline="true")
    embed.add_field(name="What is a member?", value="A member is someone that reaches out to a listener for support", inline="true")
    embed.add_field(name="What is a listener?", value="A listener is someone that has signed up to be there for others", inline="true")
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
    embed = discord.Embed(title="Help", color=0xcba3e8)
    embed.add_field(name="Place Holder", value="PLace holder", inline=False) # Need to add actually helpful messages here
    await interaction.response.send_message(embed=embed)
discord_client.run(config.discord_application_token)

