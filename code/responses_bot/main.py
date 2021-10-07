# -*- coding: utf-8 -*-

import discord
import requests
import json
import keep_alive as ka
import nest_asyncio
nest_asyncio.apply()

client = discord.Client()

verbos = [
  'llevar',
  'vacuna',
  'hisop',
  'romp',
  'analiz',
  'invertir',
  'hack',
  'haciendo',
  'hacer',
  'estudi',
  'jugar',
  'ayuda',
  'lol'
  ]

respuestas = [
  'Allá la estan llevando',
  'Allá la estan vacunando',
  'Allá la estan hisopando',
  'Allá la estan analizando',
  'Allá la estan invirtiendo',
  'Allá la estan hackeando',
  'A tu jermu se lo estan haciendo',
  'Allá se lo estan haciendo',
  'Alla la están estudiando',
  'Allá la están estudiando',
  'Con tu corazón estan jugaron',
  'Allá la están ayudando',
  'Cómo vas a jugar al lol. Virgo. No la pones más'
  ]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

@client.event
async def on_ready():
  print('We have logged as {0.user} and are reeeaadddy to kill some meatbags'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  
  if message.content.startswith('$como estas bot chupapija?'):
    await message.channel.send('los muchachos peronistas todos unidos triunfaremos')
  
  if message.content.startswith('$trolo'):
    quote = get_quote()
    await message.channel.send('mira aca te pongo una frase de trolo:\n' + quote)
  
  for i, word in enumerate(verbos):
    if i and word in message.content:
      await message.channel.send(respuestas[i])
  if 'drunken bot' in message.content:
      await message.channel.send('Mi nombre se escribe con mayúsculas, puto')
  if 'Drunken Bot' in message.content:
      await message.channel.send('Decime qué necesitas mi rey.')

ka.keep_alive()

client.run('ODk0MDkxMzE2OTE1NDg2NzQw.YVk9bQ.at1_mjaKiAZdOq0tBCNfuVzVc4k')