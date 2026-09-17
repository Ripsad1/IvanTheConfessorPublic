from discord.ext import commands

class Wordle(commands.Cog):
    WORDLE_CHANNEL_ID = 1544329108828196884
    WORDLE_BOT_ID = 1211781489931452447

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(self.WORDLE_CHANNEL_ID)

        if channel is None:
            print("Channel nicht gefunden.")
            return

        async for msg in channel.history(limit=20):
            if msg.author.id != self.WORDLE_BOT_ID:
                continue
            print(f"Von: {msg.author}\n"
                  f"Author ID: {msg.author.id}\n"
                  f"Content: {msg.content}")

def setup(bot):
    bot.add_cog(Wordle(bot))