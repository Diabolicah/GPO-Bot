"""Core of the discord bot."""
import discord
from discord.ext import commands
from pretty_help import PrettyHelp
import config as c

__author__ = "Diabolica"
intents = discord.Intents.default()
intents.members = True
startup_extensions = ["config", "commands_miscellaneous", "commands_ticketing", "commands_roblox"]
bot = commands.Bot(intents=intents, command_prefix=c.prefix, description="Grand Quest Helper is an assistant bot for the Grand Quest Games Community.", owner_id=c.bot_owner_id, case_insensitive=True)
bot.help_command = PrettyHelp(dm_help=True, no_category="Default", show_index=False, show_hidden=False, color=discord.Color.from_rgb(r=41, g=28, b=115))


# Events
@bot.event
async def on_ready():
    print('''
    +--------------------------------+ 
    | GrandQuestHelper has logged in |
    +--------------------------------+
    ''')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='Try {}help command'.format(c.prefix)))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        cd = round(error.retry_after) + 1
        await ctx.reply('This command is on cooldown for {0:d} more second{1}.'.format(cd, 's' if cd != 1 else ''), delete_after=c.delete_timer)
    if isinstance(error, commands.CheckFailure):
        await ctx.reply('You\'re unable to do that!', delete_after=c.delete_timer)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('This command is missing required arguments.', delete_after=c.delete_timer)


@bot.event
async def on_message(message):
    await process_command(message)


@bot.event
async def on_message_edit(old_message, new_message):
    if old_message.content == new_message.content:
        return
    await process_command(new_message)


@bot.command()
@commands.is_owner()
async def Reload(ctx):
    """Reloads the extensions of the bot."""
    success = True
    for ext in startup_extensions:
        print('{} has been reloaded'.format(ext))
        try:
            bot.reload_extension(ext)
        except Exception as ex:
            success = False
            try:
                await ctx.author.send('Failed to load extension {0}\n{1}: {2}'.format(ext, type(ex).__name__, str(ex)))
            finally:
                pass
    await ctx.author.send('Commands reloaded successfully!' if success else 'Something went wrong! :sob:')


# Functions
async def process_command(message):
    if message.author == bot.user:
        return
    for command_line in message.content.split('\n{0}'.format(c.prefix)):
        if command_line == message.content.split('\n{0}'.format(c.prefix))[0] and not command_line.startswith(c.prefix):
            continue
        if not command_line.startswith(c.prefix):
            command_line = "{0}{1}".format(c.prefix, command_line)
        message.content = command_line
        if message.content:
            command = message.content.split()[0].replace(c.prefix, "")
            message.content = message.content.replace(command, command.lower())
            try:
                if bot.get_command(command):
                    await message.delete(delay=0.25)
            finally:
                pass
        await bot.process_commands(message)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {0}\n{1}: {2}'.format(extension, type(e).__name__, str(e)))
    bot.run(c.token)

