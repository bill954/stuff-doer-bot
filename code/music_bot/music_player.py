import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import os
import asyncio
import nest_asyncio
nest_asyncio.apply()

client = commands.Bot(command_prefix="!")

playlist = []

# def add_to_list(url):
#     playlist.append(url)


# @client.command()
# async def p(ctx, url):
#     if not url.startswith('https://www.youtube.com'):
#         await ctx.send('That ain\'t no youtube url.')
#     if not playlist:
#         add_to_list(url)    

#     for i in playlist:
#         asyncio.create_task(ctx, playlist[i])
        

# ver 3 of player function
# pro: play online without the need of downloads
# cons: I still dont understand some lines of the code
@client.command(brief="Plays a single video, from a youtube URL")
async def play(ctx, url):
    '''
    This function recieves ctx and an url from youtube and starts playing
    audio in the same voice channel as the user who invoked it.

    '''
    channel = ctx.message.author.voice.channel
    print('este es el canal', channel)
    
    # the bot wil try to connect to the same channel voice as the user who
    # invoked the function
    # if it is already connected, it will go on
    # the except does nothing, didn't want to raise an error code here
    try:
        await channel.connect()
    except:
        print('Bot already connected to a voice channel')
    
    # this dict configures the quality and format of the audio
    # it belongs to youtube_dl, go check their documentation for mor info
    ydl_opts = {'format': 'bestaudio',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
                }],
                'noplaylist':'True'}
    
    # another dict, this one controls the ffmpeg converter (check ffmpeg doc for info)
    ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    # this will take the true url we are going to need to play the audio online
    # without needing to download it
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    # still don't know how this one works, but it gives the player the info they need
    URL = info['formats'][0]['url']
    
    # finally play the damn audio
    voice.play(discord.FFmpegPCMAudio(URL, **ffmpeg_opts))

# The add_to_list function will be the next main function of this program
# This is the idea:
#       The bot will recieve any url and put it in a list that is initialized
#   as empty in the begining of this program. Then it will autoplay any song
#   in the list and eliminating it until the list is empty again.
#   Everytime someone invokes the 'play' function they won't be actually
#   invoking play, but the add_to_list function.

@client.command()
async def add_to_list(ctx, url, playlist = playlist):
    asyncio.create_task(true_play(ctx, url))

@client.command()
async def true_play(ctx, url):
    await ctx.send('this is going to be the true player')

# the next functions are pretty generic, all they do is check the voice client
# status and do what the user asked for if they can or return a "I can't do
# this, senpai"-like message if not

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("I'm not connected to any voice channel madafaka.")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Can't pause, there ain't nothing to pause.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Audio is already playing, dummy.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('ODk0MDkxMzE2OTE1NDg2NzQw.YVk9bQ.at1_mjaKiAZdOq0tBCNfuVzVc4k')