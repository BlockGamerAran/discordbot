"""
An example module for future contributors to reference using commands.
"""
from discord.ext import commands


class ExampleCommandModule(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):

        empty_array = []
        modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

        if message.author == client.user:
            return
        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" + message.display_name + "]")

                for file in files:
                    await modmail_channel.send(file.url)
            else:
                await modmail_channel.send("<@" + str(message.author.id) + "> > " + message.content)

        elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
            member_object = message.mentions[0]
            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("[" + message.author.display_name + "]")

                for file in files:
                    await member_object.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]
                await member_object.send("[" + message.author.display_name + "]" + mod_message)


def setup(bot):
    """
    Function called by load_extension method on the bot.
    This is used to setup a discord module.
    """
    bot.add_cog(ExampleCommandModule(bot))
