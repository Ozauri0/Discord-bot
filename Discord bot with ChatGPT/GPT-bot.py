import discord
from discord.ext import commands
from config import TOKEN, API_KEY
import aiohttp



TOKEN = TOKEN.DISCORD_TOKEN #discord key
API_KEY = API_KEY.GPT_KEY #chat-gpt key

bot = commands.Bot(command_prefix="$", intents= discord.Intents.all())

#verify if bot is connected.
@bot.event
async def on_ready():
    print("Bot connected to discord succesfully!.")

###Commands###


@bot.command()
async def gpt(ctx: commands.Context, *promt: str):
    async with aiohttp.ClientSession() as session:
        message = await ctx.send("I'm proccesing your prompt...") #bot send this message when anyone uses $gpt command
        payload = {
            "model": "text-davinci-003",
            "prompt": " ".join(promt),
            "temperature": 0.5, #here you can change imagination level of answers there's level from 0 to 1, 0 is less creative and 1 is more creative. 
            "max_tokens": 2000, #max characters that you can receive in discord, the max in discord is 2000 don't overpass it.
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
        }
        headers = {"Authorization": f"Bearer {API_KEY}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            await message.delete()
            if "choices" not in response:
                await ctx.reply("I don't found a answer for your question.")
                return
            text = response["choices"][0]["text"]
            text = text.replace('\n', '\n')
            embed = discord.Embed(title="ChatGPT's answer:", description=f"```python\n{text}\n```")
            await ctx.reply(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)
