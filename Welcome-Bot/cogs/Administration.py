import discord
from discord import client
from discord import channel
from discord import message
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands


class Administration(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # command to allows the admin to kick members
    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self,ctx, member: discord.Member, *, reason = None):
        await member.kick(reason= reason)
        await ctx.send(f"user {member} has been kicked and {reason}")

    # this will print a message if you don't have the admin role
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissons to kick people")


    # command to allows the admin to ban members
    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await member.ban(reason= reason)
        await ctx.send(f"user {member} has been banned and {reason}")


    # this will print a message if you don't have the admin role
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissons to ban people")



def setup(client):
    client.add_cog(Administration(client))
