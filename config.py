import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyrogram client config
    API_ID    = os.environ.get("API_ID", "3335796")
    API_HASH  = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5088657122:AAGXARfg6sSX1p1ge876jknkrJizwH959b4") 
   
    # database config get this from mongodb
    DB_NAME = os.environ.get("DB_NAME","Dxbotz")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")
 
    BOT_UPTIME  = time.time()
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001792962793"))
    LOG_GROUP = int(os.environ.get("LOG_GROUP", "False"))
    DUMP_GROUP  = int(os.environ.get("DUMP_GROUP", "False"))
