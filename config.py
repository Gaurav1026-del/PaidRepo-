# +++ Made By King [telegram username: @Shidoteshika1] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7161957864:AAErebqAoAizEq2naLMhWcDENN-8rUn6Irw")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID",  "26571426"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", " b9a1955c10923d47a97e6656a824e41c ")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002694720727"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "6093336723"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hunter1026:N2rhIhbglW379qpi@cluster0.hg49k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DB_NAME = os.environ.get("DATABASE_NAME", "heavy")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://telegra.ph/file/5094c60f1122bbae9b3d9.jpg https://telegra.ph/file/463501fe337f02dc034ba.jpg https://telegra.ph/file/ad3486519fd59f73f7f46.jpg https://telegra.ph/file/8d4867e3d7d8e8db70f73.jpg https://telegra.ph/file/3b8897b58d83a512a56ac.jpg https://telegra.ph/file/11115f9a5c035e2d90bd8.jpg https://telegra.ph/file/a292bc4b99f9a1854f6d7.jpg https://telegra.ph/file/94aac0f8141dc44eadfc6.jpg https://telegra.ph/file/1f8d855fb7a70b4fcaf68.jpg https://telegra.ph/file/849b567f8072117353c5c.jpg https://telegra.ph/file/e8555407480d52ac1a6b7.jpg https://telegra.ph/file/2a301e221bf3c800bb48c.jpg https://telegra.ph/file/faefbf4a710eb05647d9c.jpg https://telegra.ph/file/6219c9d5edbeecfd3a45e.jpg https://telegra.ph/file/db1f952a28b0aa53bedb1.jpg https://telegra.ph/file/32797f53236187e9f5e1f.jpg https://telegra.ph/file/f1038a205b9db5018f1aa.jpg https://telegra.ph/file/88fb9950df687ff6caa58.jpg https://telegra.ph/file/63855c358fdd9a02c717c.jpg https://telegra.ph/file/34fb4b74d70bfc2e9d59c.jpg https://telegra.ph/file/e92c0b6efb0a77b316e04.jpg https://telegra.ph/file/2f3adfb321584ad39fd15.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

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
