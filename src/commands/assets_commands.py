from discord.ext.commands import Context, Bot, Cog, command
from utils.play_audio import play_asset_audio


class AssetsCommands(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name='merda', help="reproduz um áudio Alborghetti falando que merda hein")
    async def que_merda(self, ctx: Context):
        await play_asset_audio(ctx, self.bot, 'que_merda.mp3')
        return

    @command(name='merda2', help="reproduz um áudio Alborghetti gritando vá a merda")
    async def va_a_merda(self, ctx: Context):
        await play_asset_audio(ctx, self.bot, 'va_a_merda.mp3')
        return

    @command(name="burro", help="reproduz um áudio do Farid Germano xingando o técnico do Grêmio")
    async def burro(self, ctx: Context):
        await play_asset_audio(ctx, self.bot, 'burro.mp3')
        return

    @command(name="damn", help="reproduz um áudio de um véio falando falando Damn Son")
    async def damn(self, ctx: Context):
        await play_asset_audio(ctx, self.bot, 'damn_son.mp3')
        return
