""" google search """

# Copyright (C) 2020-2022 by gudmeong@Github, < https://github.com/gudmeong >.
# All rights reserved.

import aiohttp, httpx, os
from userge import userge, Message

REST_API = os.environ.get("REST_API", "")
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/61.0.3163.100 Safari/537.36"
}
ses = aiohttp.ClientSession()
http = httpx.AsyncClient(
    http2=True,
    timeout=httpx.Timeout(20)
)

async def get(url: str, *args, **kwargs):
    async with ses.get(url, *args, **kwargs) as res:
        try:
            data = res.json()
        except Exception:
            data = res.text()
    return data

@userge.on_cmd("gs", about={
    'header': "do a Google search",
    'usage': "{tr}gs [query | reply to msg]",
    'examples': "{tr}gs What is Async"})
async def gsearch(message: Message):
    query = message.filtered_input_str
    if message.reply_to_message:
        query = message.reply_to_message.text
    if not query:
        await message.err("Give a query or reply to a message to google!")
        return
    await message.edit(f"**Googling** for `{query}` ...")
    html = await http.get(f"{REST_API}/google?q={query}", headers=head)
    rjson = html.json()
    if not rjson.get('result'):
        await message.edit(f"Not Found for `{query}` Maybe API down")
        return
    result = "".join(f"**{no}.** [{item['tite']}]({item['link']})\n{item['snippet']}\n\n" for no, item in enumerate(rjson['result'], start=1))
    output = f"**Google Search:**\n`{query}`\n\n**Results:**\n{result}"
    await message.edit_or_send_as_file(
        text=output,
        caption=query,
        disable_web_page_preview=True
    )
    
