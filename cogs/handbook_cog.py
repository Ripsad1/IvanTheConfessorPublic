import discord
from discord.ext import commands

class Handbook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.handbook = ("help -> handbook\n"
                "random daily -> wählt eine zufällige aufgabe aus IMC und IMO")

    def build_embed(self):
        embed = discord.Embed(
            title="Handbook",
            description="This bot features the following commands:",
            color=discord.Color.purple()
        )
        embed.add_field(
            name="help",
            value="shows this handbook",
            inline=False)
        embed.add_field(
            name="random daily",
            value="chooses a random IMC or IMO problem",
            inline=False,
        )
        embed.add_field(
            name="list [Endung]",
            value="shows all saved german words ending in 'al'",
            inline=False
        )
        return embed

    @discord.slash_command(
        name = "handbook",
        description = "Shows handbook"
    )
    async def handbook(self,ctx):
        if ctx.author.bot:
            return
        await ctx.respond(embed=self.build_embed())




def setup(bot):
    bot.add_cog(Handbook(bot))