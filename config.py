# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23595172"))
API_HASH = getenv("API_HASH", "d4c35b7ef112914876fc34eceb4dfe2d")
BOT_TOKEN = getenv("BOT_TOKEN", "7790205099:AAERzB_u5SJcU_skHs6iBFG7tNsd3P4-yQM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7002735087").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://cluster:efAbVEB6oUXUsJu7@cluster0.twhpwa4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002446291556")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002204110324"))
