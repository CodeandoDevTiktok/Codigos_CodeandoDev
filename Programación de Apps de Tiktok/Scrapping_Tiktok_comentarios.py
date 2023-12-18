from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

cliente = TikTokLiveClient("@angelo.gamer")

async def comentarios(event: CommentEvent):
    print(f"COMENTARIO: {event.user.nickname} --> {event.comment}")

cliente.add_listener("comment", comentarios)

cliente.run()

