from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.errors import SessionPasswordNeededError
import os
import asyncio
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import SessionPasswordNeededError

# Replace these with your own values
api_id = 21156118
api_hash = '36544b3fe9b0176b3ab2d672a27fb732'
phone_number = '7007761008'
channel_username = '@Free ENGLISH BY NEETU SINGH'

async def download_channel_content():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        try:
            # Connect to Telegram
            await client.start(phone_number)

            # Retrieve the channel entity
            channel = await client.get_entity(channel_username)

            # Create a folder for downloads if it doesn't exist
            if not os.path.exists('downloads'):
                os.makedirs('downloads')

            # Get all the messages from the channel
            async for message in client.iter_messages(channel):
                # Check if the message has media
                if message.media:
                    # Download the media
                    await client.download_media(message.media, file=f'downloads/{message.id}')

        except SessionPasswordNeededError:
            print('This account is protected by two-step verification. Please enter your password below:')
            pw = input()
            await client.start(phone_number, password=pw)

# Run the download function
asyncio.run(download_channel_content())