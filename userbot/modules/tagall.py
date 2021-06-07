# U S Σ R Δ T O R / Ümüd

import time
import requests

from collections import deque
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from time import sleep
from random import choice, getrandbits, randint
from re import sub
from userbot import CMD_HELP, bot, SUDO_ID
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.tagall$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()


@register(outgoing=True, pattern="^.taq(.*)")
@register(incoming=True, from_users=SUDO_ID, pattern="^.taq(.*)")
async def tagallcmd(event):
  if event.pattern_match.group(1):
    tag = event.pattern_match.group(1)
  else:
    tag = ""
  await event.delete()
  tags = []
  async for user in event.client.iter_participants(event.chat_id, 750):
   tags.append(f"[{user.first_name}](tg://user?id={user.id})\n")
  chunkss = list(chunks(tags, 6))
  random.shuffle(chunkss)
  for chunk in chunkss:
   await event.client.send_message(event.chat_id, '\u2060'.join(chunk)+tag)
   sleep(1.5)


def chunks(lst, n):
 for i in range(0, len(lst), n):
  yield lst[i:i + n]


@register(outgoing=True, pattern="^.admin")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp('tagall').add_command(
    'tagall', None, 'Hərkəsi bir mesajda tağ edər.'
).add_command(
    'tag', None, 'Hərkəsi bir-bir tağ edər.'
).add_command(
    'admin', None, 'Bu əmri hər hansıxa sohbətdə işlədəndə adminləri tağ edər.'
).add()
