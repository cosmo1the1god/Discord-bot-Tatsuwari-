import disnake
from disnake.ext import commands
from disnake import TextInputStyle


class TAG(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    class MyModal(disnake.ui.Modal):
        def __init__(self):
            # The details of the modal, and its components
            components = [
                disnake.ui.TextInput(
                    label="Name",
                    placeholder="NAME OF Tag",
                    custom_id="name",
                    style=TextInputStyle.short,
                    max_length=50,
                ),
                disnake.ui.TextInput(
                    label="Description",
                    placeholder="Lorem ipsum dolor sit amet.",
                    custom_id="description",
                    style=TextInputStyle.paragraph,
                ),
            ]
            super().__init__(
                title="Create Tag",
                custom_id="create_tag",
                components=components,
            )

        # The callback received when the user input is completed.
        async def callback(self, inter: disnake.ModalInteraction):
            embed = disnake.Embed(title="Tag Creation")
            for key, value in inter.text_values.items():
                embed.add_field(
                    name=key.capitalize(),
                    value=value[:1024],
                    inline=False,
                )
            await inter.response.send_message(embed=embed)

    @commands.slash_command()
    async def tags(self, inter: disnake.AppCmdInter):
        """Sends a Modal to create a tag."""
        await inter.response.send_modal(modal=self.MyModal(), delete_after=50)


def setup(bot: commands.bot):
    bot.add_cog(TAG(bot))
