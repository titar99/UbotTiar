import os

API_ID = int(os.getenv("API_ID", "29509596"))
API_HASH = os.getenv("API_HASH", "07719f967f31a6dfe739c170fa32f319")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7428426730:AAHmMoNSMlKcLOJPOhGSQifq2PRsGajMV-Y")
OWNER_ID = int(os.getenv("OWNER_ID", "6853143041"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002171403395"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888 -1001571197486").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "40"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://titar:fadhil123@cluster0.ppxf2yw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
