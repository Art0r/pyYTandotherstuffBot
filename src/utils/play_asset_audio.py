import os
from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from time import sleep


async def play_asset_audio(ctx: Context, bot: Bot, title: str) -> None:
    if ctx.author != bot.user:
        try:
            voice_channel = ctx.author.voice
            if voice_channel is not None:
                vc = await voice_channel.channel.connect()
                vc.play(FFmpegPCMAudio(os.path.join(os.path.dirname(
                    __file__), '..', '..', 'assets', title)))
                while vc.is_playing():
                    sleep(.1)
                await vc.disconnect()
            else:
                await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
        except:
            await vc.disconnect()
