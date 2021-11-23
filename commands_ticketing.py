import asyncio

from discord.ext import commands
import discord

import datetime


class TicketingCommandsCog(commands.Cog, name="Ticketing Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def Ticket(self, ctx):
        """This command allows you to open up a ticket and forward it to a staff member.

                This command allows you to open up a ticket to appeal a ban, request a restore or report a person.

                Usage: Ticket
        """
        appeal_emoji = "📌"
        restore_emoji = "🎫"
        lock_emoji = "🔒"
        one_emoji = ":one:"
        two_emoji = ":two:"
        three_emoji = ":three:"

        message_embed = discord.Embed(color=discord.Color.from_rgb(r=66, g=135, b=245))
        message_embed.title = "Ticket"
        message_embed.description = "Which type of ticket would you like to open?"
        message_embed.set_footer(text=datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")+" UTC+0", icon_url=self.bot.user.avatar_url)
        message_embed.add_field(name="{} Appeal".format(appeal_emoji), value="Black Marketing\nExploiting\nScamming\n­", inline=False)
        message_embed.add_field(name="{} Restore".format(restore_emoji), value="Fruit\nRobux Products\n­", inline=False)
        message_embed.add_field(name="{} Report".format(lock_emoji), value="Exploiter\nScammer\n­", inline=False)

        sent_message = await ctx.author.send(embed=message_embed)

        bot: commands.Bot = self.bot

        await sent_message.add_reaction(emoji=appeal_emoji)
        await sent_message.add_reaction(emoji=restore_emoji)
        await sent_message.add_reaction(emoji=lock_emoji)

        try:
            def checkReaction(payload: discord.RawReactionActionEvent):
                if payload.user_id != bot.user.id and sent_message.id == payload.message_id:
                    return True

            payload: discord.RawReactionActionEvent = await bot.wait_for("raw_reaction_add", timeout=30.0, check=checkReaction)

            emoji_name = (
                payload.emoji.name
                if payload.emoji.id is None
                else f":{payload.emoji.name}:{payload.emoji.id}"
            )
            if payload.user_id == ctx.author.id and emoji_name in (appeal_emoji, restore_emoji, lock_emoji):
                try:
                    await sent_message.remove_reaction(emoji=appeal_emoji, member=bot.user)
                    await sent_message.remove_reaction(emoji=restore_emoji, member=bot.user)
                    await sent_message.remove_reaction(emoji=lock_emoji, member=bot.user)
                    await sent_message.remove_reaction(emoji=payload.emoji, member=discord.Object(id=payload.user_id))
                except discord.errors.Forbidden:
                    pass

                if payload.emoji.name == appeal_emoji:
                    message_embed.title = "Appeal Ticket"
                    message_embed.description = "Which type of appeal ticket would you like to open?"
                    message_embed.clear_fields()
                    message_embed.add_field(name="Appeal", value="{} Black Marketing\n{} Exploiting\n{} Scamming\n­".format(one_emoji, two_emoji, three_emoji), inline=False)
                    await sent_message.edit(embed=message_embed)
                if payload.emoji.name == restore_emoji:
                    message_embed.title = "Restore Ticket"
                    message_embed.description = "Which type of appeal ticket would you like to open?"
                    message_embed.clear_fields()
                    message_embed.add_field(name="Restore", value="{} Fruit\n{} Products\n­".format(one_emoji, two_emoji), inline=False)
                    await sent_message.edit(embed=message_embed)
                if payload.emoji.name == lock_emoji:
                    message_embed.title = "Report Ticket"
                    message_embed.description = "Which type of appeal ticket would you like to open?"
                    message_embed.clear_fields()
                    message_embed.add_field(name="Report", value="{} Exploiter\n{} Scammer\n­".format(one_emoji, two_emoji), inline=False)
                    await sent_message.edit(embed=message_embed)
            else:
                try:
                    await sent_message.edit(embed=discord.Embed(color=discord.Color.from_rgb(r=66, g=135, b=245), title="Ticket Discarded"))
                    await sent_message.remove_reaction(emoji=appeal_emoji, member=bot.user)
                    await sent_message.remove_reaction(emoji=restore_emoji, member=bot.user)
                    await sent_message.remove_reaction(emoji=lock_emoji, member=bot.user)
                except Exception:
                    pass

        except asyncio.TimeoutError:
            try:
                await sent_message.edit(embed=discord.Embed(color=discord.Color.from_rgb(r=66, g=135, b=245), title="Ticket Discarded"))
                await sent_message.remove_reaction(emoji=appeal_emoji, member=bot.user)
                await sent_message.remove_reaction(emoji=restore_emoji, member=bot.user)
                await sent_message.remove_reaction(emoji=lock_emoji, member=bot.user)
            except Exception:
                pass


def setup(bot):
    bot.add_cog(TicketingCommandsCog(bot))
