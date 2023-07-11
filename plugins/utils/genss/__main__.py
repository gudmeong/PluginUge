""" generate screenshot """

# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.


import os
import random
import asyncio, string

from hachoir.metadata import extractMetadata as XMan
from hachoir.parser import createParser as CPR 
from pyrogram.types import InputMediaPhoto

from userge import userge, Message, config
from userge.utils import take_screen_shot, progress

def ranword(length: int = 5):  # noqa: E252
    text_str = "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))
    return text_str.upper()
    


@userge.on_cmd("genss", about={
    'header': "Screen Shot Generator",
    'description': "Generate Random Screen Shots from any video "
                   " **[NOTE: If no frame count is passed, default"
                   " value for number of ss is 5. ",
    'usage': "{tr}genss [No of SS (optional)] [Path or reply to Video]"})
async def ss_gen(message: Message):
    replied = message.reply_to_message
    vid_loc = ''
    ss_c = 5
    should_clean = False
    await message.edit("Checking you Input?🧐🤔😳")
    if message.input_str:
        if ' ' in message.input_str:
            ss_c, vid_loc = message.input_str.split(" ", 1)
        else:
            try:
                ss_c = int(message.input_str)
            except ValueError:
                vid_loc = message.input_str

    if not vid_loc and replied:
        if not (
            replied.video
            or replied.animation
            or (replied.document and "video" in replied.document.mime_type)
        ):
            await message.edit("I doubt it is a video")
            return
        await message.edit("Downloading Video to my Local")
        vid = await message.client.download_media(
            message=replied,
            file_name=config.Dynamic.DOWN_PATH,
            progress=progress,
            progress_args=(message, "Downloading🧐? W8 plox")
        )
        vid_loc = os.path.join(config.Dynamic.DOWN_PATH, os.path.basename(vid))
        should_clean = True
    await message.edit("Compiling Resources")
    meta = XMan(CPR(vid_loc))
    if meta and meta.has("duration"):
        vid_len = meta.get("duration").seconds
    else:
        await message.edit("Something went wrong, Not able to gather metadata")
        return
    await message.edit("Done, Generating Screen Shots and uploading")
    PHOTO = []
    try:
        for frames in random.sample(range(vid_len), int(ss_c)):
            rword = ranword(7)
            capture = await take_screen_shot(vid_loc, int(frames), "ss_cap.jpeg")
            PHOTO.append(InputMediaPhoto("ss_cap.jpeg"))
        await message.reply_media_group(media=PHOTO, reply_to_message_id=message.id)
        os.remove(capture)
        await message.edit("Uploaded")
        PHOTO.clear()
    except Exception as e:
        await message.edit(e)
    if should_clean:
        os.remove(vid_loc)
