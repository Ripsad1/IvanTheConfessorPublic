import discord
import random
from discord.ext import commands

COMPETITIONS = {
    "IMO": {"years": [y for y in range(1959, 2026) if y != 1980], "problems": 6},
    "IMC": {"years": list(range(1994, 2026)), "problems": 10},
}


class RandomTask(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name = "random_daily",
        description = "chooses a random IMC or IMO problem"
    )
    async def random_daily(self,
                           ctx:discord.ApplicationContext,
                           competition:discord.Option(
                               str,
                               "choose a competition",
                               choices=["IMO","IMC","random"]
                           )
                           ):
        if competition == "random":
            competition = random.choice(["IMO", "IMC"])
        data = COMPETITIONS[competition]
        year = random.choice(data["years"])
        number = random.randint(1,data["problems"])
        await ctx.respond(f"{competition}-{year}-{number}")


def setup(bot):
    bot.add_cog(RandomTask(bot))