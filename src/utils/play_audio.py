import os
from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from discord.channel import VoiceChannel
from discord.member import Member, VoiceState
from pafy import new
from pafy.pafy import Pafy
from pafy.backend_youtube_dl import YtdlStream

active_channel_connection: VoiceChannel = None


def play(func):
    async def _play(ctx: Context, bot: Bot, url: str = ""):
        if ctx.author != bot.user:
            try:
                author: Member = ctx.author
                author_voice: VoiceState = author.voice
                voice_channel: VoiceChannel = author_voice.channel
                if voice_channel is not None:
                    global active_channel_connection
                    if active_channel_connection is None:
                        voice_connection = await voice_channel.connect()
                        active_channel_connection = voice_connection
                        await func(ctx, bot, url, voice_connection)
                    else:
                        await func(ctx, bot, url, active_channel_connection)
                else:
                    await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
                    return
            except Exception as e:
                # COMMENT ON PRODUCTION
                await ctx.reply(e.args[0])
                await active_channel_connection.disconnect()
                return
    return _play


@play
async def play_audio_from_url(ctx: Context, bot: Bot, url: str, conn=None) -> None:
    audio: Pafy = new(url)
    audio_stream: YtdlStream = audio.getbestaudio()
    conn.play(
        FFmpegPCMAudio(audio_stream.url))
    return


@play
async def stop_audio(ctx: Context, bot: Bot, url: str = "", conn=None) -> None:
    conn.stop()
    return


@play
async def play_asset_audio(ctx: Context, bot: Bot, title: str, conn=None) -> None:
    conn.play(FFmpegPCMAudio(os.path.join(os.path.dirname(
        __file__), '..', '..', 'assets', title)))
    return
