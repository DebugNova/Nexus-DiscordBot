import discord
import openai
import os
import json
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Load persistent memory from a JSON file
try:
    with open("memory.json", "r") as f:
        memory = json.load(f)
except FileNotFoundError:
    memory = {}

# Save memory to JSON for persistence
def save_memory():
    with open("memory.json", "w") as f:
        json.dump(memory, f)

# Function to add to memory
def add_to_memory(key, value):
    memory[key] = value
    save_memory()

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Track channels where the bot is "awake"
awake_channels = set()

# Conversation history per channel
conversation_history = {}

# OpenAI Chat Completion with context
async def ask_Nexus(channel_id, question):
    """Send a question to OpenAI and include the remembered context."""
    # Prepare OpenAI messages
    messages = [{"role": "system", "content": "You are Nexus, an empathetic assistant. You are 2 weeks old and designed to understand emotions. Respond with compassion and practical help, emotionally aware replies while talking professional and talk in concise and very short manner."}]

    # Add conversation history for the channel
    if channel_id in conversation_history:
        for entry in conversation_history[channel_id]:
            messages.append(entry)

    # Append the user's question
    messages.append({"role": "user", "content": question})

    # Get OpenAI response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        reply = response['choices'][0]['message']['content']

        # Update conversation history
        if channel_id not in conversation_history:
            conversation_history[channel_id] = []
        conversation_history[channel_id].append({"role": "user", "content": question})
        conversation_history[channel_id].append({"role": "assistant", "content": reply})

        return reply
    except Exception as e:
        return f"Error: {e}"

# Detect if the message implies memory
def detect_memory_intent(message):
    patterns = [
        r"my name is (\w+)",
        r"call me (\w+)",
        r"remember that (.+) is (.+)",
        r"please remember that (.+)",
        r"can you remember (.+)",
        r"make a note that (.+)",
        r"my nickname is (\w+)",
        r"from now on, call me (\w+)",
        r"i want you to remember (.+)",
        r"write this down: (.+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return match.groups()  # Return the captured groups for saving in memory
    return None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(
        activity=discord.Game(name="Master of memory!🤖✨"),
        status=discord.Status.online
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    global awake_channels

    query = message.content.strip()

    # Wake-up command
    if query.lower() == "nexus wake up":
        awake_channels.add(message.channel.id)
        if message.channel.id not in conversation_history:
            conversation_history[message.channel.id] = []
        await message.channel.send("I am awake and ready to assist, Sir.")
        return

    # Sleep command
    if query.lower() == "nexus sleep":
        if message.channel.id in awake_channels:
            awake_channels.remove(message.channel.id)
            await message.channel.send("Going to sleep, Sir. Call me anytime.")
        return

     # Respond only if in an awake channel
    if message.channel.id in awake_channels:
        # Process as regular query
        response = await ask_Nexus(message.channel.id, query)
        await message.channel.send(response)

# Run the bot
client.run(DISCORD_TOKEN)
