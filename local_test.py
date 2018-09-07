#simple bot for testing local server hosting

import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author != self.user:
            print('Message from {0.author}: {0.content)'.format(message))

client = MyClient()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
