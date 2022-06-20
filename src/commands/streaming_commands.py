from discord.ext.commands import Context, Bot, Cog, command
from utils.play_yt_audio import play_audio_from_url


class StreamingCommands(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot
