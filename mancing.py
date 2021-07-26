#!/usr/bin/env python3
import time, asyncio, sys


from telethon import TelegramClient, events, utils

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'casino'

Casino = 'All Sea'

    
with TelegramClient(sesi_file, api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('KampungMaifamBot', Casino))

    @client.on(events.NewMessage(from_users='KampungMaifamBot'))
    async def handler(event):
        if 'Bagian kecil' in event.raw_text:
            time.sleep(1)
            await event.click(text='Tarik Jala')
            return
        
        if 'Kamu berhasil menangkap' in event.raw_text:
            time.sleep(1)
            await event.respond('All Sea')
            return
        
        if 'Kamu tidak memiliki cukup energi' in event.raw_text:
            time.sleep(1)
            await event.respond('/restore_max')
            return
        
        if 'Restore 4000 energi' in event.raw_text:
            time.sleep(1)
            await event.click(text='Confirm')
            return
        
        if 'Energi berhasil ' in event.raw_text:
            time.sleep(1)
            await event.respond('All Sea')
            return
        
        if 'Tunggu minimal' in event.raw_text:
            time.sleep(1)
            await event.respond('/fishpoint_500')
            return
        
        if 'Berhasil membeli' in event.raw_text:
            time.sleep(1)
            await event.respond('/umpanjala_1000')
            return
        
        if 'Kamu membeli' in event.raw_text:
            time.sleep(1)
            await event.respond('All Sea')
            return
        
    client.start() 
    client.run_until_disconnected() 
    print(time.asctime(), '-', 'berhenti')
	
	