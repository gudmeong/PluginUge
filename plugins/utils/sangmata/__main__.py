""" check user name or username history """

# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

# By @Krishna_Singhal

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message
from userge.utils.exceptions import StopConversation


@userge.on_cmd("sg", about={
    'header': "Sangmata gives you user's last updated names and usernames.",
    'flags': {
        '-u': "To get Username history of a User"},
    'usage': "{tr}sg [Reply to user]\n"
             "{tr}sg -u [Reply to user]"}, allow_via_bot=False)
async def sangmata_(message: Message):
    """ Get User's Updated previous Names and Usernames """
    if replied:
        user = replied.from_user.id
    else:
        user = message.input_str
    if user.startswith("@"):
        user = (await message.client.get_users(user.split("@")[1])).id
    chat = "@SangMata_beta_bot"
    if not user:
        await message.err("```\nReply or input id or username to get Name and Username History...```", del_in=5)
        return
    await message.edit("```\nGetting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked {chat}, Unblock it".format(chat=chat)
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message(f"{user}")
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(mark_read=True))
            msgs.append(await conv.get_response(timeout=3, mark_read=True))
    except StopConversation:
        pass
    for msg in msgs:
        if '-u' in message.flags:
            if msg.text.startswith("No data available"):
                await message.edit("```\nUser never changed his Username...```", del_in=5)
                return
            username = msg.text.split("Usernames")[1]
            await message.edit(username)
        else:
            if msg.text.startswith("No data available"):
                await message.edit("```\nUser never changed his Name...```", del_in=5)
                return
            name = msg.text.split("Names")[1].split("Usernames")[0]
            await message.edit(name)
