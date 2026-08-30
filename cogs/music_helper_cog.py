import discord
from discord.ext import commands
import random
from collections import deque
import string
from helper.dict_saver_and_loader import load_dict, save_dict
from helper.condition_checker import condition_checker
from helper.interpreter import interpreter


class MusicHelper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_10_messages = deque(maxlen=10)

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.author.bot:
            return

        MUSIC_HELPER_FILE = "helper/music_helper.json"
        music_dict = load_dict(MUSIC_HELPER_FILE)
        content = msg.content.lower()

        for command in music_dict:
            condition = music_dict[command]["condition"]
            if condition_checker(content, condition):
                await msg.channel.send(interpreter(msg, music_dict[command]["write"]))


def setup(bot):
    bot.add_cog(MusicHelper(bot))