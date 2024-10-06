# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23595172"))
API_HASH = getenv("API_HASH", "d4c35b7ef112914876fc34eceb4dfe2d")
BOT_TOKEN = getenv("BOT_TOKEN", "7797834536:AAED4H8rdpBMtgPgl5NmPZc-IlJMlPhilmI")
OWNER_ID = int(getenv("OWNER_ID", "7002735087"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://techmonofficial:techmon123@cluster0.ga2uy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002323134166"))
FORCESUB = getenv("FORCESUB", "ForceSub1000")
