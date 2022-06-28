class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs </b><a href=https://t.me/{}><b>{}</b></a><b>,𝙸 ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs 🎥 ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ</b>"""
    HELP_TXT = """<b>𝙷𝙴𝚈 {},
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs.<b/>"""
    ABOUT_TXT = """❤️ <b>Mʏ Nᴀᴍᴇ : {}
🎭 Uᴘᴅᴀᴛᴇs : <a href=https://t.me/M2LINKS>ᴍ𝟸ʟɪɴᴋs</a></b>"""
  


    MANUELFILTER_TXT = """<b>𝙷ᴇʟᴘ : ᴍᴀɴᴜᴀʟ Fɪʟᴛᴇʀ</b>

Fɪʟᴛᴇʀ ɪs ᴛʜᴇ Fᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs Fᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴇᴠᴀᴍᴀʀɪᴀ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs Fᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ

<b>N͏O͏T͏E͏:</b>
𝟷. ɪ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ. 
𝟸. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ Fɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ. 
𝟹. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>:ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """𝙷ᴇʟᴘ: <b>Buttons</b>

ɪ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>NOTE:</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ. 
𝟸. ɪ ᴡɪʟʟ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ. 
𝟹. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:https://t.me/Media_Search_Bot)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>𝙷ᴇʟᴘ : ᴀᴜᴛᴏ Fɪʟᴛᴇʀ</b>

<b>NOTE:</b>
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪF ɪᴛ's ᴘʀɪᴠᴀᴛᴇ. 
𝟸. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ Fᴀᴋᴇ Fɪʟᴇs. 
𝟹. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ϙᴜᴏᴛᴇs.  ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ Fɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    CONNECTION_TXT = """<b>𝙷ᴇʟᴘ : ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

𝟷.ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ Fᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀᴤ  
𝟸.ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘᴤ.

<b>NOTE:</b>
𝟷. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
𝟸. sᴇɴᴅ <code>/connect</code> Fᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴘᴍ

<b>:ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """<b>𝙷ᴇʟᴘ : ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs</b>

<b>:ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🎥 T𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂  : <code>{}</code>
🙎‍♂️ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂 : <code>{}</code>
📊 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂 : <code>{}</code>
⏹ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
✅ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
