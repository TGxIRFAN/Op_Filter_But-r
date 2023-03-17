class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍

ᠰMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏᠰ: <a href='https://telegram.me/im_goutham_josh'>Gᴏᴜᴛʜᴀᴍ ᠰSᴇʀ</a>
"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/wudixh13'>Gᴏᴜᴛʜᴀᴍ ᠰSᴇʀ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://dashboard.heroku.com/'>Hᴇʀᴏᴋᴜ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.7.1 [ Sᴛᴀʙʟᴇ ]</b>"""
    
    SOURCE_TXT = """<b>ɴᴏᴛᴇ:
- ꜱᴏᴜʀᴄᴇ - <a href="ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ">ʜᴇʀᴇ</a>
Dᴇᴠᴇʟᴏᴘᴇʀ:
- <a href="https://t.me/wudixh13">Gᴏᴜᴛʜᴀᴍ ᠰSᴇʀ</a></b>"""
    
    
    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.
<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""
    
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""


    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    LOGO = """
    
                  
██╗░░██╗██╗░░░██╗████████╗████████╗██╗░░░██╗██████╗░░█████╗░████████╗
██║░██╔╝██║░░░██║╚══██╔══╝╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝
█████═╝░██║░░░██║░░░██║░░░░░░██║░░░██║░░░██║██████╦╝██║░░██║░░░██║░░░
██╔═██╗░██║░░░██║░░░██║░░░░░░██║░░░██║░░░██║██╔══██╗██║░░██║░░░██║░░░
██║░╚██╗╚██████╔╝░░░██║░░░░░░██║░░░╚██████╔╝██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚═════╝░░╚════╝░░░░╚═╝░░░




▒█▀▄▀█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀ 　 ▒█▀▀█ ▒█░░▒█ 　 ▒█▀▀█ ▒█▀▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█░▒█ ░█▀▀█ ▒█▀▄▀█ 　 ▒█▀▀▀█ 　 ▒█▀▀▀ 　 ▒█▀▀█ 
▒█▒█▒█ ▒█▄▄█ ▒█░▒█ ▒█▀▀▀ 　 ▒█▀▀▄ ▒█▄▄▄█ 　 ▒█░▄▄ ▒█░░▒█ ▒█░▒█ ░▒█░░ ▒█▀▀█ ▒█▄▄█ ▒█▒█▒█ 　 ░▀▀▀▄▄ 　 ▒█▀▀▀ 　 ▒█▄▄▀ 
▒█░░▒█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ 　 ▒█▄▄█ ░░▒█░░ 　 ▒█▄▄█ ▒█▄▄▄█ ░▀▄▄▀ ░▒█░░ ▒█░▒█ ▒█░▒█ ▒█░░▒█ 　 ▒█▄▄▄█ 　 ▒█▄▄▄ 　 ▒█░▒█"""
