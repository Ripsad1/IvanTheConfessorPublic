import discord
from discord.ext import commands
import random
from collections import deque
import string
from helper.dict_saver_and_loader import load_dict, save_dict
from helper.condition_checker import condition_checker
from helper.interpreter import interpreter


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_10_messages = deque(maxlen=10)

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.author.bot:
            return

        COMMANDS_FILE = "helper/commands.json"
        MUSIC_HELPER_FILE = "helper/music_helper.json"
        commands_dict = load_dict(COMMANDS_FILE)
        music_dict = load_dict(MUSIC_HELPER_FILE)
        content = msg.content.lower()
        possible_messages = []

        for command in commands_dict:
            condition = commands_dict[command]["condition"]
            if command in self.last_10_messages:
                continue
            else:
                if condition_checker(content,condition):
                    possible_messages.append(command)
        if len(possible_messages) == 0:
            return None
        if len(possible_messages) > 0:
            choice = random.choice(possible_messages)
            commands_dict[choice]["times_triggered"] += 1
            save_dict(COMMANDS_FILE, commands_dict)
            if commands_dict[choice]["spam_prevent"] == 1:
                self.last_10_messages.append(choice)
            await msg.channel.send(interpreter(msg, commands_dict[choice]["write"]))


def setup(bot):
    bot.add_cog(Moderation(bot))