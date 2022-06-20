from datetime import datetime
from os import getenv
from dotenv import load_dotenv
from discord.ext.commands import Bot, Context, CommandError
from commands.assets_commands import AssetsCommands
from commands.other_commands import OtherCommands
from commands.streaming_commands import StreamingCommands

load_dotenv()
token = getenv('TOKEN')

bot = Bot(command_prefix=getenv('PREFIX'))


@bot.event
async def on_ready():
    print(f'{bot.user} está rodando')
    return


@bot.event
async def on_command(ctx: Context):
    print(f"""
    {getenv("PREFIX")}{ctx.command} - by {ctx.author} in {ctx.channel}|{ctx.guild} at {datetime.now().strftime("%d/%m/%y %H:%M:%S")}
    """)
    return


# @bot.event
# async def on_command_error(ctx: Context, err: CommandError):
#    await ctx.reply(err.args[0])
#    return

bot.add_cog(StreamingCommands(bot))
bot.add_cog(AssetsCommands(bot))
bot.add_cog(OtherCommands(bot))
bot.run(token)
