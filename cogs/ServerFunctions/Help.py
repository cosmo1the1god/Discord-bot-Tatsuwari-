import disnake
from disnake.ext import commands


class HelpMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        """Get help with the bot."""
        futures = ["```ping,",
                   "userinfo ///@user,",
                   "server-info,",
                   "tags,",
                   "mini-games,",
                   "bic_kurs",
                   "Clear, Clears the chat with amount can you give how many msg he dose to del"
                   "wikipedia,",
                   "weather,",
                   "translator,",
                   "search,",
                   "ban, you must have mod permissions,",
                   "kick, you must have mod permissions,",
                   "create_role/mod_create_role/admin_create_role, ///colour like green, black, grey, dark_green,",
                   "create_text_channel/create_voice_channel, you must have admin permissions,",
                   "unban, you must have mod permissions,",
                   "timeout, you must have mod permissions,",
                   "remove_roles, you must have admin permissions,///!remove_roles @User  @name_of_role reason,",
                   "add_roles, you can add basic role with out any permission, ///!add_roles @User  @name_of_role "
                   "reason,",
                   "Ping```"]

        embed = disnake.Embed(title="Tatsuwari Features ✓", description="The Most Features has slahs command: /",
                              colour=0x299aa6)
        embed.add_field(name="Features", value='```\n```'.join(futures), inline=True)
        await inter.send(embed=embed, delete_after=50)


def setup(bot: commands.bot):
    bot.add_cog(HelpMe(bot))
