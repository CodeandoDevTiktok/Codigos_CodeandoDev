from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

cliente = TikTokLiveClient("@lttqzd2002")

async def comentarios(event: CommentEvent):
    print(f"COMENTARIO: {event.user.nickname} --> {event.comment}")

cliente.add_listener("comment", comentarios)

cliente.run()

