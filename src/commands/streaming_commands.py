from discord.ext.commands import Context, Bot, Cog, command
from utils.play_audio import play_audio_from_url, stop_audio


class StreamingCommands(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="play", help="Toca uma música a partir de uma url do youtube")
    async def play(self, ctx: Context):
        await play_audio_from_url(ctx=ctx, bot=self.bot, url="https://www.youtube.com/watch?v=zzfA4QUIHVY")
        return

    @command(name="stop", help="Para o aúdio sendo tocado")
    async def stop(self, ctx: Context):
        await stop_audio(ctx, self.bot)
        return
