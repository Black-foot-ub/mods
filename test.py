from blackfoot import loader, utils


class SomeTestMod(loader.Module):
    "TEst"
    
    strings = {
        "name": "LGBTGovno"
    }
    
    async def somecmd(self, client, message):
        await message.delete()
