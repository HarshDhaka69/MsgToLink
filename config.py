



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6402498262:AAE9YKYkbuJ_XNxsWpeXFE_p_1TtHha5QnI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29988716"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f0dba98fa5aaa7ff345a4069968684c9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002020466241"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5190315686"))

#Port
PORT = os.environ.get("PORT", "18080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://itsharshx432:itsharshx432@itsharshx432.vxcphnl.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002076368866"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002094091607"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʏ {mention}\n\nꜱᴇɴᴅ ᴍᴇ ᴀɴʏᴛʜɪɴɢ ɪ'ʟʟ ɢɪᴠᴇ ʏᴏᴜ ɪᴛ'ꜱ ᴘᴇʀᴍᴀɴᴇɴᴛ ꜱʜᴀʀᴀʙʟᴇ ʟɪɴᴋ.​</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {mention}\n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ\n\nᴋɪɴᴅʟʏ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ​</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>​🇧​​🇴​​🇹​ ​🇺​​🇵​​🇹​​🇮​​🇲​​🇪​</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1917604476)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
