# MADE BY AMAN PANDEY FOR DYNAMIC USERBOT DONT KANG.
from DYNAMIC import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from DYNAMIC.utils import load_module
from DYNAMIC.utils import start_assistant
from DYNAMIC import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("DYNAMIC USERBOT STABLE VERSION STARTING")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("DYNAMIC USERBOT STARED SUCESSFULLY")
        print("LOADING SOFTWARE")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Loading Software Completed")
        print("LOADING HIDDEN FILES")
        print ('INSTALLING ALL STABLE VERSION OF DYNAMIC USERBOT AND PLUGINS')
    else:
        bot.start()
async def op():
  import glob
  path = 'DYNAMIC/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))

import DYNAMIC._core

bot.loop.run_until_complete(op())
print("DYNAMIC LOADED HIDDEN FILES, SOFTWARE WITH SUCESS JOIN SUPPORT FOR MORE INFO @DYNAMICUSERBOTSUPPORT ")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
