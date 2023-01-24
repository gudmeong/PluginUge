import requests, os, lk21, re
from userge import userge, Message, pool
from pyrogram import enums


@pool.run_in_thread
def fembed(url: str) -> str:
    scraper = lk21.Bypass()
    result = ""
    try:
        urls = scraper.bypass_fembed(url)
        for no, item in enumerate(list(urls), start=1):
            result += f"**{no}.** Reso: {item} -> `{urls[item]}`\n\n"
        return result
    except Exception as f:
        result += f"ERROR.fembed:\n\n{str(f)}"
        return result

@pool.run_in_thread
def stape(url: str) -> str:
    url = url.replace(".xyz", ".com")
    result = ""
    scraper = lk21.Bypass()
    try:
        bypasser = scraper.bypass_streamtape(url)
        result += f"streamtape:\n`{bypasser}`"
        return result
    except Exception as s:
        result += f"ERROR.stape: {s}"
        return result


"""
@userge.on_cmd("cdl", about={
    'header': "Custom DirectDownloadLink",
    'supported links': ['streamtape(aliases), fembed(aliases)'],
    'usage': "{tr}sdl [link] {tr}fdl [link]"}
    )
 async def cdl_(m: Message):
    pass
 """
    
@userge.on_cmd("sdl", about={
    'header': "Generate streamtape ddl",
    'supported links': ['ONLY streamtape(aliases)'],
    'usage': "{tr}sdl [link]"}
    )
async def sdl_(m: Message):
    """ Custom DirectDownloadLink streamtape """
    text = m.input_or_reply_str
    if not text:
        await m.err("input not found! Denied.")
        return
    await m.edit("`Processing streamtape...`")
    links = re.findall(r'\bhttps?://.*\.\S+', text)
    if not links:
        await m.err("No valid links found!")
        return
    result = f"**Custom DirectDownloadLink:**\n\n"
    for link in links:
        try:
            res = await stape(link)
            result += f"Original Link `{link}`\n\nResult:\n\n{res}"
        except Exception as e:
            result += f"ERROR.sdl_:\n\n{str(e)}"
    await m.edit(result, parse_mode=enums.ParseMode.MARKDOWN)


@userge.on_cmd("fdl", about={
    'header': "Generate fembed ddl",
    'supported links': ['ONLY fembed(aliases)'],
    'usage': "{tr}fdl [link]"}
    )
async def fdl_(m: Message):
    """ Custom DirectDownloadLink fembed """
    text = m.input_or_reply_str
    if not text:
        await m.err("input not found! Denied.")
        return
    await m.edit("`Processing fembed...`")
    links = re.findall(r'\bhttps?://.*\.\S+', text)
    if not links:
        await m.err("No valid links found!")
        return
    result = f"**Custom DirectDownloadLink:**\n\n"
    for link in links:
        try:
            res = await fembed(link)
            result += f"Result:\n\n{res}"
        except Exception as e:
            result += f"ERROR.fdl_:\n\n{str(e)}"
    await m.edit(result, parse_mode=enums.ParseMode.MARKDOWN)
            
            