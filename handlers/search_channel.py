from models.inspector_models import FoundClientByInspector
from models.link_models import ChatJoinRequest, LinkFactoryLink, LinkFactoryBot, Channel
from models.postback_models import Postback


async def search_channel(user_id):
    postback: Postback = await Postback.filter(
        user_id=user_id, sub1__not_isnull=True).first()
    if postback:
        chat_join_req: ChatJoinRequest = await ChatJoinRequest.filter(
            uid=postback.sub1, link_id__not_isnull=True).first()
        if chat_join_req:
            link: LinkFactoryLink = await chat_join_req.link
            first_ever_request_link: LinkFactoryLink = await (
                LinkFactoryLink.filter(id=link.id).first())
            if first_ever_request_link:
                _bot: LinkFactoryBot = await first_ever_request_link.bot
                channel: Channel = await _bot.channel
                await FoundClientByInspector.create(
                    uid=user_id, channel_id=channel.id)
