import requests, os, lk21, re
from userge import userge, Message, pool
from pyrogram import enums

STREAMTAPE = [
        "streamtape.",
        "strtape.cloud",
        "streamta.pe",
        "strcloud.link",
        "strtpe.link",
        "scloud.online",
        "stape.fun",
        "streamtapeadblock.art",
        "streamadblockplus.com",
        "shavetape.cash",
        "streamtape.xyz"
    ]
    
FEMBED = [
    "fembed.net",
    "fembed.com",
    "fembad.org",
    "femax20.com",
    "fcdn.stream",
    "feurl.com",
    "naniplay.nanime.in",
    "naniplay.nanime.biz",
    "naniplay.com",
    "layarkacaxxi.icu",
    "dutrag.com",
    "cumpletlyaws.my.id",
    "mrdhan.com",
    "mm9842.com",
    "diasfem.com",
    "mycloudzz.com",
    "asianclub.tv",
    "iframe1videos.xyz",
    "watchjavnow.xyz",
    "kotakajair.xyz",
    "suzihaza.com",
    "javsubs91.com",
    "youtnbe.xyz",
    "nekolink.site",
    "2tazhfx9vrx4jnvaxt87sknw5eqbd6as.club",
    "watch-jav-english.live",
    "streamabc.xyz",
    "ns21.online",
    "dbfilm.bar",
    "panenjamu.xyz",
    "gdplayer.xyz",
    "44324242.xyz",
    "play.dubindo.site",
    "lk12.my.id",
    "komikhentai.eu.org",
    "tpxanime.in",
    "javlove.club",
    "pusatporn.live",
    "anime789.com",
    "24hd.club",
    "vcdn.io",
    "sharinglink.club",
    "votrefiles.club",
    "femoload.xyz",
    "dailyplanet.pw",
    "jplayer.net",
    "xstreamcdn.com",
    "gcloud.live",
    "vcdnplay.com",
    "vidohd.com",
    "vidsource.me",
    "votrefile.xyz",
    "zidiplay.com",
    "mediashore.org",
    "there.to",
    "sexhd.co",
    "viplayer.cc",
    "votrefilms.xyz",
    "embedsito.com",
    "youvideos.ru",
    "streamm4u.club",
    "moviepl.xyz",
    "vidcloud.fun",
    "fplayer.info",
    "moviemaniac.org",
    "albavido.xyz",
    "ncdnstm.com",
    "fembed-hd.com",
    "superplayxyz.club",
    "cinegrabber.com",
    "ndrama.xyz",
    "javstream.top",
    "javpoll.com",
    "ezsubz.com",
    "reeoov.tube",
    "diampokusy.com",
    "nazbz.my.id",
    "gfilm21.xyz",
    "gudangmovies21asli.xyz",
    "lajkema.com",
    "filmvi.xyz",
    "rapidplay.org",
    "cloudrls.com",
    "sf21.cyou",
    "bebasbiaya.net",
    "vidsrc.xyz",
    "streamhoe.online",
    "i18n.pw",
    "henkasuru.my.id",
    "savefilm21info.xyz",
    "luxubu.review",
    "vanfem.com",
    "playerjavseen.com",
    "vid21.vip",
    "bbfilm.xyz",
    "lkc21.net",
    "subtitleufr.com",
    "javcl.me",
    "kitabmarkaz.xyz",
    "dataku.win"
]

@userge.on_cmd("cdl", about={
    'header': "Generate a custom DDL",
    'supported links': [
          'fembed(aliases', 'streamtape(aliases)'
        ],
    'usage': "{tr}cdl [link]"})
async def cdl_(m: Message):
    """ Custom DirectDownloadLink """
    text = m.input_or_reply_str
    if not text:
        await m.err("input not found!")
        return
    await m.edit("`Processing...`")
    links = re.findall(r'\bhttps?://.*\.\S+', text)
    if not links:
        await m.err("No links found!")
        return
    result = f"**Custom DirectDownloadLink:**\n\n"
    for link in links:
        try:
            if all(f for f in FEMBED):
                result += f"Results: {await fembed(link)}\n"
            elif all(s for s in STREAMTAPE):
                result += f"Results: {await stape(link)}\n"
            else:
                result += f"Results: {link} Not Supported DirectDownloadLink\n"
        except Exception as e:
            result += f"ERROR.cdl:\n\n{str(e)}"
    await m.edit(result, parse_mode=enums.ParseMode.MARKDOWN)
            
            
@pool.run_in_thread
def fembed(url: str) -> str:
    scraper = Bypass()
    result = ""
    try:
        urls = scraper.bypass_fembed(url)
        result += "".join(f"Original link: {url}\nfembed:\n**{no}.** {item} -> {urls[item]}\n\n" for no, item in enumerate(list(urls), start=1))
        return result
    except Exception as f:
        result += f"ERROR.fembed:\n\n{str(f)}"
        return result

@pool.run_in_thread
def stape(url: str) -> str:
    url = url.replace(".xyz", ".com")
    result = ""
    scraper = Bypass()
    try:
        bypasser = scraper.bypass_streamtape(url)
        result += f"streamtape:\n{bypasser}"
        return result
    except Exception as s:
        result += f"ERROR.streamtape: {s}"
        return result