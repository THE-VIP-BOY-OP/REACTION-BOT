import asyncio
from pyrogram import Client, idle
from .logger import LOGGER
from config import BOT_TOKENS, API_HASH, API_ID
from typing import Callable, Optional

import pyrogram

log = LOGGER(__name__)

class Bots:
    def __init__(self):
        self.tokens = BOT_TOKENS
        self.clients = []
        self.client_ids = []

    async def start(self):
        self.clients.clear()
        self.client_ids.clear()
        log.info("Starting bots...")

        for i, token in enumerate(self.tokens, start=1):
            client = Client(
                f"client_{i}",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=token,
                plugins=dict(root="VIPMUSIC/plugins"),
                in_memory=True,
            )
            await client.start()
            log.info(f"Bot {i} as Started as {client.me.first_name}")

            self.clients.append(client)
            self.client_ids.append(client.me.id)

    async def stop(self):
        for client in self.clients:
            await client.stop()
        self.clients.clear()
        self.client_ids.clear()

    def setup(self):
        loop = asyncio.get_event_loop_policy().get_event_loop()
        async def start():
            await self.start()
            await idle()
            log.info("Stoping All bots...\nGoodBye")
            await self.stop()

        loop.run_until_complete(start())


    def on_cmd(
        filters: Optional[pyrogram.filters.Filter] = None, group: int = 0
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            for client in self.clients:
                client.add_handler(pyrogram.handlers.MessageHandler(func, filters), group)
            return func

        return decorator