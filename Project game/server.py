from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent

username = "username_tiktok"
client = TikTokLiveClient(unique_id=username)

@client.on("gift")
def on_gift(event: GiftEvent):
    gift_name = event.gift.name.lower()

    if gift_name == "Rose":
        print("Comand")
    elif gift_name == "Heart":
        print("love")
    elif gift_name == "paus":
        print("paus")

client.run()