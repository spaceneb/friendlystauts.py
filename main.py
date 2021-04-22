import discord
import asyncio
token = "your_token_here"
async def run_loop(self):
    while True:
        memberCount = 0
        for guild in client.guilds:
            memberCount = memberCount + guild.member_count
        await client.change_presence(activity=discord.Game(name=f"Click | {self.user} | {len(client.guilds)} Servers | Users {str(memberCount)} | Friends {len(self.user.friends)} | Blocking {len(self.user.blocked)}",start=self.user.created_at))
        if client.get_guild(830803221756772424).get_member(776983528821882911).status != discord.Status.offline:
            blocks = []
        await asyncio.sleep(60)
intents = discord.Intents.default()
intents.members = True
constructor_client = discord.Client
constructor_client.intents = intents
class ConstructClient(constructor_client):
    async def on_ready(self):
        print('User = {0}'.format(self.user))
        await run_loop(self)
                

client = ConstructClient()
client.run(token,bot=False)