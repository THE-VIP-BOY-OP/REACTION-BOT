import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

from VIPMUSIC import app

# List of reactions
reactions = [
    "👍", "👎", "❤️", "🔥", "🥳", "👏", "😁", "😂", "😲", "😱", 
    "😢", "😭", "🎉", "😇", "😍", "😅", "💩", "🙏", "🤝", "🍓", 
    "🎃", "👀", "💯", "😎", "🤖", "🐵", "👻", "🎄", "🥂", "🎅", 
    "❄️", "✍️", "🎁", "🤔", "💔", "🥰", "😢", "🥺", "🙈", "🤡", 
    "😋", "🎊", "🍾", "🌟", "👶", "🦄", "💤", "😷", "👨‍💻", "🍌", 
    "🍓", "💀", "👨‍🏫", "🤝", "☠️", "🎯", "🍕", "🦾", "🔥", "💃"
]


@app.on_message(filters.text)
async def react_to_message(client: Client, message: Message):
    """
    This function reacts to any message with a random reaction from the 'reactions' list.
    """
    
    emoji = random.choice(reactions)
    await message.react(emoji)
