from tortoise import fields
from tortoise.models import Model

from base_models import BaseObjectModel


class LinkFactoryUser(BaseObjectModel):

    class Meta:
        schema = "link_factory"
        table = "user"
        table_description = "Users of the LinkFactory"


class Channel(BaseObjectModel):
    user: fields.ForeignKeyRelation[LinkFactoryUser] = fields.ForeignKeyField(
        "link_factory.LinkFactoryUser", related_name="channels", null=True, on_delete=fields.SET_NULL
    )

    class Meta:
        schema = "link_factory"
        table = "channel"
        table_description = "Telegram Channel"


class LinkFactoryBot(BaseObjectModel):
    token = fields.CharField(max_length=64, unique=True, description="Unique Telegram bot authentication token")

    user: fields.ForeignKeyRelation[LinkFactoryUser] = fields.ForeignKeyField(
        "link_factory.LinkFactoryUser", related_name="bots", null=True, on_delete=fields.SET_NULL
    )
    channel: fields.ForeignKeyRelation[Channel] = fields.ForeignKeyField(
        "link_factory.Channel", related_name="bots", null=True, on_delete=fields.SET_NULL
    )

    class Meta:
        schema = "link_factory"
        table = "bot"
        table_description = "Bots added by users"


class LinkFactoryLink(Model):
    id = fields.IntField(pk=True)
    link = fields.CharField(max_length=64)
    name = fields.CharField(max_length=32)
    created_at = fields.DatetimeField(auto_now_add=True)
    title = fields.CharField(max_length=30, default="")
    bot: fields.ForeignKeyRelation[LinkFactoryBot] = fields.ForeignKeyField(
        "link_factory.LinkFactoryBot", related_name="links", null=True, on_delete=fields.SET_NULL
    )

    class Meta:
        schema = "link_factory"
        table = "link"
        table_description = "Link"

    def __str__(self):
        return self.link


class ChatJoinRequest(BaseObjectModel):
    is_request = fields.BooleanField() #public channel - False, private channel - True
    link: fields.ForeignKeyRelation[LinkFactoryLink] = fields.ForeignKeyField(
        "link_factory.LinkFactoryLink", related_name="chat_join_requests", null=True, on_delete=fields.SET_NULL
    )

    class Meta:
        schema = "link_factory"
        table = "chat_join_request"
        table_description = "Chat join requests"
        unique_together = (("uid", "link"),)
