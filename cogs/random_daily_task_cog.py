import random
from discord.ext import commands

COMPETITIONS = {
    "IMO": {"years": [y for y in range(1959, 2026) if y != 1980], "problems": 6},
    "IMC": {"years": list(range(1994, 2026)), "problems": 10},
}


class RandomTask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return

        if msg.content.strip().lower() == "random daily":
            name = random.choice(list(COMPETITIONS))
            data = COMPETITIONS[name]
            year = random.choice(data["years"])
            number = random.randint(1, data["problems"])
            await msg.channel.send(f"{name}-{year}-{number}")


def setup(bot):
    bot.add_cog(RandomTask(bot))