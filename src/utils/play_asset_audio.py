import os
from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from time import sleep
from discord.channel import VoiceChannel
from discord.member import Member, VoiceState


async def play_asset_audio(ctx: Context, bot: Bot, title: str) -> None:
    if ctx.author != bot.user:
        try:
            author: Member = ctx.author
            author_voice: VoiceState = author.voice
            voice_channel: VoiceChannel = author_voice.channel
            if voice_channel is not None:
                vc = await voice_channel.connect()
                vc.play(FFmpegPCMAudio(os.path.join(os.path.dirname(
                    __file__), '..', '..', 'assets', title)))
                while vc.is_playing():
                    sleep(1)
                await vc.disconnect()
                return
            else:
                await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
                return
        except:
            await vc.disconnect()
            return
