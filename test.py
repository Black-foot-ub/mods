from blackfoot import loader, utils


class SomeTestMod(loader.Module):
    "TEst"
    
    async def somecmd(self, client, message):
        await message.delete()
