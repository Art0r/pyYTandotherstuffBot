from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from time import sleep
from discord.channel import VoiceChannel
from discord.member import Member, VoiceState
from pafy import new
from pafy.pafy import Pafy
from pafy.backend_youtube_dl import YtdlStream

activate_channel_connection: VoiceChannel = None


async def play_audio_from_url(ctx: Context, bot: Bot, url: str) -> None:
    if ctx.author != bot.user:
        try:
            author: Member = ctx.author
            author_voice: VoiceState = author.voice
            voice_channel: VoiceChannel = author_voice.channel
            if voice_channel is not None:
                global activate_channel_connection
                if activate_channel_connection is None:
                    voice_connection = await voice_channel.connect()
                    activate_channel_connection = voice_connection
                    audio: Pafy = new(url)
                    audio_stream: YtdlStream = audio.getbestaudio()
                    voice_connection.play(
                        FFmpegPCMAudio(audio_stream.url))
                    return
                else:
                    audio: Pafy = new(url)
                    audio_stream: YtdlStream = audio.getbestaudio()
                    activate_channel_connection.play(
                        FFmpegPCMAudio(audio_stream.url))
                    return
            else:
                await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
                return
        except Exception as e:
            await ctx.reply(e.args[0])
            await voice_connection.disconnect()
            return


async def stop_audio(ctx: Context, bot: Bot) -> None:
    if ctx.author != bot.user:
        try:
            author: Member = ctx.author
            author_voice: VoiceState = author.voice
            voice_channel: VoiceChannel = author_voice.channel
            if voice_channel is not None:
                global activate_channel_connection
                activate_channel_connection.stop()
                return
            else:
                await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
                return
        except Exception as e:
            await ctx.reply(e.args[0])
            await activate_channel_connection.disconnect()
            return
