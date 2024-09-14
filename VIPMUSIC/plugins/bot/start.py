import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

# List of reactions
reactions = [
    "👍", "👎", "❤️", "🔥", "🥳", "👏", "😁", "😂", "😲", "😱", 
    "😢", "😭", "🎉", "😇", "😍", "😅", "💩", "🙏", "🤝", "🍓", 
    "🎃", "👀", "💯", "😎", "🤖", "🐵", "👻", "🎄", "🥂", "🎅", 
    "❄️", "✍️", "🎁", "🤔", "💔", "🥰", "😢", "🥺", "🙈", "🤡", 
    "😋", "🎊", "🍾", "🌟", "👶", "🦄", "💤", "😷", "👨‍💻", "🍌", 
    "🍓", "💀", "👨‍🏫", "🤝", "☠️", "🎯", "🍕", "🦾", "🔥", "💃"
]

@Client.on_message(filters.group, group=1)
async def react_to_message(client: Client, message: Message):
    emoji = random.choice(reactions)
    await message.react(emoji)


@Client.on_message(filters.command(["start", "help"]))
async def start_help_command(client: Client, message: Message):
    await message.reply_text("I am an auto reaction bot. Add me in group or channels for auto react on your posts.")