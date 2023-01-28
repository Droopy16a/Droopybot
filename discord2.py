import openai
import discord
import requests
import json
from discord.ext import commands
# Authenticate with OpenAI API
openai_api_key = "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"

# Define a function to generate a response to a message
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.5,
        api_key=openai_api_key
    )

    message = completions.choices[0].text
    print(message)
    return message

# Create a Discord client
client = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@client.event

async def on_message(message):
    # If the message is from the bot itself, ignore it
    if message.author == client.user:
        return
    if message.guild is None:
        prompt = message.content
        print(message.content)
        await message.channel.send("Ok just wait a minute...")
        try:
            response = generate_response(prompt)
            await message.channel.send(response)
        except:
            await message.channel.send("ERROR please try again")
# Run the bot
discord_token = "OTk5MDAwNTQ2ODkzNjM5NzUz.G5yDTK.V-p8ZfTxm4U3XRIk2ph1C6iEEMSzuL6CbMz-J0"
client.run(discord_token)