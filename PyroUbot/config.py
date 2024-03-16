import os

API_ID = int(os.getenv("API_ID", "17896688"))
API_HASH = os.getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6905616591:AAHiaI_DHby8h0bXvpIOy1EuhziWTr0O7zM")
OWNER_ID = int(os.getenv("OWNER_ID", "1948147616"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001904601620"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001969856888 -1001571197486").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "40"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://baseFWB:fadhil123@cluster0.9dpso7g.mongodb.net/?retryWrites=true&w=majority",
)
