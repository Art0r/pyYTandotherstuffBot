from os import getenv
from discord.ext.commands import Context, Bot, Cog, command


class OtherCommands(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name='ping', help="responde a mensagem com pong")
    async def ping(self, ctx: Context, *args):
        if ctx.author != self.bot.user:
            await ctx.reply('pong')
        return

    @command(name='source', help="responde com o link para o GitHub do projeto")
    async def source(self, ctx: Context):
        if ctx.author != self.bot.user:
            await ctx.reply(getenv('SOURCE'))
        return
