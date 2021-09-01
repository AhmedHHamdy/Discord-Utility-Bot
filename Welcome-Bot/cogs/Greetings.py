import discord
from discord import client
from discord import channel
from discord import emoji
from discord import message
from discord import member
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    #command Hello Command
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Hello There")

    #event greetings when joining the server  
    @commands.Cog.listener()
    async def on_member_join(self,member, guild):
        general_channel = self.client.get_channel(881305758770266125)
        await general_channel.send("Welcome To The Server")

    #event goodbye when some leave the server  
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        general_channel = self.client.get_channel(881305758770266125)
        await general_channel.send("Goodbye")
 
    #event when someone submit a reaction, the bot announces it
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
       channel = reaction.message.channel 
       await channel.send(user.name + " added: " + str(reaction.emoji)) 

    #event when someone remove a reaction, the bot announces it
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
       channel = reaction.message.channel 
       await channel.send(user.name + " remove: " + str(reaction.emoji)) 

    #event when someone type the name of emoji
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        
        if "thumbs up" in message.content:
            emoji = '\U0001F44D'
            await message.add_reaction(emoji) 

    


def setup(client):
    client.add_cog(Greetings(client))