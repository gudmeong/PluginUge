import shutil, psutil, asyncio, aiofiles

from userge import userge, Message, pool
from pyrogram import enums
from userge.utils import humanbytes

@userge.on_cmd("mod", about={
    'header': "Other self mods haha v0.5",
    'description': "Unofficial modules for Userge",
    'usage': "{tr}st\n{tr}copy [link]"}
)
async def checkmsg(m: Message):
    msg = await m.edit("`Processing ...`", parse_mode=enums.ParseMode.MARKDOWN)
    await asyncio.sleep(1)
    return await msg.edit("**Are you drunk? haha**")


@userge.on_cmd("st", about={
    'header': 'Checking Statistics',
    'usage': '{tr}st'}
)
async def bstat(m: Message):
    msg = await m.edit("`Processing Checking Server Statistics ...`", parse_mode=enums.ParseMode.MARKDOWN)
    proc = await sys_info()
    await msg.edit(proc)

@userge.on_cmd("copy", about={
    'header': 'Copy message...',
    'usage': '{tr}copy [link]'
    }
)
async def copied(msg: Message):
    link = msg.input_str
    await msg.edit("Processing...")
    if not link:
        return await msg.edit("Input LINK BLOG")
    res = link.split("/")
    try:
        cid, mid = res[4], res[5]
    except:
        cid, mid = res[3], res[4]
    if cid.isdigit():
        cid = f"-100{cid}"
    gmsg = await msg.client.get_messages(str(cid), int(mid))
    if gmsg.chat.has_protected_content and gmsg.photo:
        photo = await gmsg.download()
        await msg.reply_photo(photo=photo, caption=gmsg.caption)
        await aiofiles.os.remove(photo)
        await msg.edit("Successfully.")
    else:
        await msg.reply_photo(photo=gmsg.photo.file_id, caption=gmsg.caption)
        await msg.edit("Successfully.")

@pool.run_in_thread
def sys_info():
    try:
        core = psutil.cpu_count()
        total, used, free = shutil.disk_usage('.')
        total, used, free = humanbytes(total), humanbytes(used), humanbytes(free)
        dl = humanbytes(psutil.net_io_counters().bytes_sent)
        ul = humanbytes(psutil.net_io_counters().bytes_recv)
        mem = psutil.virtual_memory()
        mavail = humanbytes(mem.available)
        mtotal = humanbytes(mem.total)
        mfree = humanbytes(mem.free)
        mused = humanbytes(mem.used)
        text = (
            f"**User/Bot Statistic**\n\n"
            f"**Cpu:**\n"
            f"`Total Core   : {core}`\n\n"
            f"**Disk Currently**\n"
            f"`Total/Avail  : {total}`\n"
            f"`Used/Free    : {used} | {free}`\n\n"
            f"**Memory Currently**\n"
            f"`Available    : {mavail}`\n"
            f"`Total        : {mtotal}`\n"
            f"`Used/Free    : {mused} | {mfree}`\n\n"
            f"**Network Counter**\n"
            f"`Download     : {dl}`\n"
            f"`Upload       : {ul}`\n"
            f"Use `.stest` for useless"
        )
        return text
    except Exception as e:
        return f"ERROR:\n{str(e)}"

# end of lines