from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent

client = TikTokLiveClient(unique_id="relsinn")

@client.on("gift")
def on_gift(event: GiftEvent):
    print(f"Gift diterima: {event.gift.name}")
client.run()