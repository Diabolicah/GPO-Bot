import pymongo
from discord.ext import commands


class ConfigCog(commands.Cog, name="Config Cog"):
    def __init__(self, bot):
        self.bot = bot


# discord variables
prefix = "`"
token = "ODE4MjI0NjE3OTEwMzA0ODA4.YEU9Dg.e7SBTXFqYNGTcqlsyXoiT3g4MmQ"
bot_owner_id = 133022153405628416
delete_timer = 1
task_timer = 300
dev_server_id = 818293905921540128
admin_server_id = 0
server_log_channel_id = 818550978730131506

# database variables
connection = pymongo.MongoClient("mongodb://localhost")
database = connection.grandquesthelperdatabase
ticket_collection = database.tickets


def setup(bot):
    bot.add_cog(ConfigCog(bot))
