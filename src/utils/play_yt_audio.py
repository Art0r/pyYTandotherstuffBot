from discord.ext.commands import Context, Bot
from discord import FFmpegPCMAudio
from time import sleep
import pafy


async def play_audio_from_url(ctx: Context, bot: Bot, url: str):
    if ctx.author != bot.user:
        try:
            voice_channel = ctx.author.voice
            if voice_channel is not None:
                vc = await voice_channel.channel.connect()
                audio = pafy.new(url)
                audio_stream = audio.getbestaudio()
                vc.play(FFmpegPCMAudio(audio_stream.url))
                while vc.is_playing():
                    sleep(1)
                await vc.disconnect()
            else:
                await ctx.reply('é necessário estar em um chat de voz para utilizar esse comando')
        except Exception as e:
            print(e.args)
            await vc.disconnect()
