from program  import client,filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

TeluguZone = Client(
    name = "Daemon",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


 print("Bot was started")

 TeluguZone.run()
