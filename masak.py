#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'masak-masak-fnz'

bot_id = 'KampungMaifamXBot'
Masak = input('Masak Apa (input command, contoh /masak_bacon_100) = ')

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Masak))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Berhasil memasak" in pesan:
                time.sleep(2)
                await event.respond(Masak)
                print(pesan)
                return
                
            
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
