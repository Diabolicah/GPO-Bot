import typing

import discord
import os
from discord.ext import commands

import config as c


async def is_admin(ctx):  # Remember to update dev server id to admin server id
    if ctx.message.author.id == c.bot_owner_id or ctx.bot.get_guild(c.dev_server_id).get_member(ctx.message.author.id) is not None:
        return True


class RobloxCommandsCog(commands.Cog, name="Roblox Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(30, 60, commands.BucketType.default)
    @commands.check(is_admin)
    async def RBan(self, ctx, user: typing.Union[int, discord.Member, discord.User, str], *,
                   reason="no reason specified"):
        """This command allows the user to ban a player from the game in roblox.

                This command allows the user to ban a player from the game in roblox.

                Usage: Ban <Discord UserName,Mention,Id,Roblox UserName, Roblox Id> <Reason>
        """
        await ctx.send("user: {}\nreason: {}\n".format(user, reason))

    @RBan.error
    async def RBan_error(self, ctx, error):
        if isinstance(error, commands.BadUnionArgument):
            await ctx.reply("User was not specified!", delete_after=c.delete_timer)


def setup(bot):
    bot.add_cog(RobloxCommandsCog(bot))
