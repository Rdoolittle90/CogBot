from typing import Any, Coroutine
from nextcord.ui import Modal, TextInput
from nextcord import Interaction


class EasyModal(Modal):
    list_num = 1
    def __init__(self, title, callback_func, **kwargs):
        self.callback_function = callback_func

        self.list_num = EasyModal.list_num
        super().__init__(
            title,
            timeout=5 * 60,
        )
        EasyModal.list_num += 1
        
        for idx, items in enumerate(kwargs.items()):
            field = TextInput(
                label=items[0],
                custom_id=f"EasyModal_{self.list_num}_{idx}",
                default_value=items[1],
                min_length=2,
                max_length=50,
            )
            self.add_item(field)

    async def callback(self, interaction: Interaction) -> Coroutine[Any, Any, None]:
        print(self.children)
        await self.callback_function(interaction, self.children)