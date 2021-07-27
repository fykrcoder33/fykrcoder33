#!/usr/bin/env python3
import time, asyncio, sys, random


from telethon import TelegramClient, events, utils, Button

api_id = 2394927 
api_hash = '4ab4c48f456d11a2aef03310c88c0b81'
sesi_file = 'tambang-fnz'

bot_id = 'KampungMaifamBot'
Area = input('Area Tambang = ')
Alat = input('Alat = ')

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "Tingkatkan kemampuan" in pesan:
                time.sleep(2)
                await event.respond(Alat)
                print(pesan)
                return
                
            elif 'Kamu tidak memiliki Energi' in pesan:
                time.sleep(2)
                await event.respond('/restore')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif "Kamu tidak memiliki bom" in pesan:
                time.sleep(2)
                await event.respond('/belixxx_bomb_1000')
                print(time.asctime(), 'Beli Bom')
                return

            if "Beli 1000" in pesan:
                time.sleep(2)
                await event.click(text='Confirm')
                print(time.asctime(), 'Berhasil Beli Bom')
                return
                
            elif 'Energi berhasil' in pesan:
                time.sleep(2)
                await event.respond(Alat)
                print('Lanjot Gan')
                return
            
            else :
                time.sleep(2)
                await event.click(text=Alat)
                print(time.asctime(), 'Lempar bom')
                print(pesan)
                return
            
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
