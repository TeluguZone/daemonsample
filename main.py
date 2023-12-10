  from program  import client,filters


  API_ID = "24830912"
  API_HASH = "a1a1775593531b90850b8b82e3b14940"
  BOT_TOKEN =    "6764321113:AAGJrZkn4r0Ll9dYaxbpkLgEOvIs9fG1UXs"

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
