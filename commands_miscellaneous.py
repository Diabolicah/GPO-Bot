import typing

import discord
import os
from discord.ext import commands

import config as c


class MiscellaneousCommandsCog(commands.Cog, name="Miscellaneous Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.check(lambda ctx: ctx.message.author.id == c.bot_owner_id or ctx.message.author.id == 259878067349094410)
    async def Sex(self, ctx, user: typing.Union[discord.Member, discord.User]):
        """This command allows TBGlitch to have his way with mentioned person.

                This command allows TBGlitch to have his way with mentioned person.

                Usage: Sex <UserName,Mention,Id>
        """
        await ctx.send("_TBGlitch had his way with {} _ :tired_face::smiling_face_with_3_hearts:".format(user.mention))

    @Sex.error
    async def Sex_error(self, ctx, error):
        if isinstance(error, commands.BadUnionArgument):
            await ctx.reply("User was not specified!", delete_after=c.delete_timer)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.check(lambda ctx: ctx.message.author.id == c.bot_owner_id or ctx.message.author.id == 293516070168297472)
    async def Bird(self, ctx):
        """This command makes the bot become a bird for a moment.

                This command allows Bird to make the bot become a bird for a moment.

                Usage: Bird
        """
        await ctx.send("Chirp-chirp~ :bird:")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.check(lambda ctx: ctx.message.author.id == c.bot_owner_id or ctx.message.author.id == 192687338810245120)
    async def Water(self, ctx):
        """This command makes the bot post water's image.

                This command allows Water to make the bot post his water image.

                Usage: Water
        """
        await ctx.send(file=discord.File(os.path.join(os.getcwd(), "Images", "Water_Image.png")))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.check(lambda ctx: ctx.message.author.id == c.bot_owner_id or ctx.message.author.id == 191794647381573632)
    async def Slap(self, ctx, user: typing.Union[discord.Member, discord.User]):
        """This command makes the bot post slap gif.

                This command allows Falcon to slap someone.

                Usage: Slap
        """
        await ctx.send("_ {} Slaps {}_".format(ctx.author.mention, user.mention), file=discord.File(os.path.join(os.getcwd(), "Images", "Falcon_Slap.gif")))

    @Slap.error
    async def Slap_error(self, ctx, error):
        if isinstance(error, commands.BadUnionArgument):
            await ctx.reply("User was not specified!", delete_after=c.delete_timer)


def setup(bot):
    bot.add_cog(MiscellaneousCommandsCog(bot))
