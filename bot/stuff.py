# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from datetime import datetime

START_TIME = datetime.now()

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**Send me the video which you want to encode.**\n**Uptime: {str(datetime.now() - START_TIME).split('.')[0]}\n\n**",
        buttons=[
            [Button.inline("♻️ HELP ♻️", data="help")],
            [Button.url("💥 OWNER 💥",url="t.me/TGxD2K")],
        ],
    )

async def zylern(event):
    await event.reply(
        f"""
**Available Commands 🤖**

/start - __Check Bot is Working Or Not__
/help - __Get Detailed Help__
/setcode - __Set Custom FFMPEG Code__
/getcode - __Print Current FFMPEG Code__
/logs - __Get Bot Logs__
/ping - __Check Ping__
/sysinfo - __Get System Info__
/leech - __Leech Links And Compress Video__
/renew - __Clear Cached Downloads__
/clear - __Clear Queued Files__
/showthumb - __Show Current Thumbnail__
/speed - __Do A SpeedTest__
/eval - __Execute An Argument__
/bash - __Run Bash Commands__
/cmds - __List Available Commands__
"""
    )


async def help(event):
    await event.edit(
        f"""**Send Me Any Video I Will Automatically Send It's Encoded Video File 😎\n\nSince Bot is on beta mode, it's a bit laggy & slow!**""",
        buttons=[
            [Button.url("Owner", url="t.me/TGxD2K")],
        ],
    )
    
async def ihelp(e):
    await e.reply(
        f"""**Send Me Any Video I Will Automatically Send It's Encoded Video File.**"""
    )
