from program  import client,filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

TeluguZone = Client(
    name = "Daemon",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@TeluguZone.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hᴇʟʟᴏ {}, ɪ ᴀᴍ ᴘᴏᴡᴇʀ ғᴜʟʟ Movie Search Bot")


@TeluguZone.on_message(filters.command("help"))
async def start_cmd(client, message):
     await message.reply_text("conatact my father @daemon990 with feel free")
    
    

                       
 print("Bot was started")

 TeluguZone.run()
