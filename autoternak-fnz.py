#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'autoternak-fnz'

bot_id = 'KampungMaifamXBot'
Area = 'Ternak'

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Daftar Ternak" in pesan:
                time.sleep(2)
                await event.respond('/ambilHasilSekarang')
                return

            elif "Kamu memperoleh:" in pesan:
                time.sleep(2)
                await event.respond('/beriMakan')
                print(pesan)
                return
                
            elif 'Kamu tidak memiliki' in pesan:
                time.sleep(2)
                await event.respond('/restore_max_confirm')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.respond(Area)
                print('Lanjot Yaaaa....')
                return
            
            else :
                time.sleep(2)
                await event.respond('/ambilHasilSekarang')
                print(time.asctime(), 'Hiiii Sayang')
                return
            
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
