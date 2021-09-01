import discord
from discord import client
from discord import channel
from discord import message
from discord import member
from discord import FFmpegPCMAudio
from discord.ext import commands


class Audio(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # command to allow the bot to join the voice channel and play audio files from your pc
    @commands.command(pass_context = True)
    async def join(self,ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
            voice = await channel.connect()
            source = FFmpegPCMAudio("4_DINERO - 120BPM - F harmonic minor.wav")
            player = voice.play(source)
        else:
            await ctx.send("You are not in a voice channel,u must be in a voice channel to run this commend")

    # command to allow the bot to leave the voice channel
    @commands.command(pass_context = True)
    async def leave(self,ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("i left the voice channel")
        else:
            await ctx.send("i am  not in a voice channel")

    # pause the audio file 
    @commands.command(pass_context = True)
    async def pause(self,ctx):
        voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("there is no audio playing")

    # resume the audio file 
    @commands.command(pass_context = True)
    async def resume(self,ctx):
        voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("there is no song is paused")
    # play the audio file 
    @commands.command(pass_context = True)
    async def play(self,ctx):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio("4_DINERO - 120BPM - F harmonic minor.wav")
        player = voice.play(source)



def setup(client):
    client.add_cog(Audio(client))