import discord
from discord import activity
from discord.ext import commands
from dotenv import load_dotenv
import os



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!",intents = intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb,activity=discord.Game("Utility-Bot"))
    print("the bot is now ready for use")
    print("-----------------------------") 


initial_extensions = []

for filename in os.listdir('C:\\Users\\Admin\\Desktop\\Bot 1\\Welcome-Bot\\cogs'):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)


client.run(TOKEN)