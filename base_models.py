from tortoise.models import Model
from tortoise import fields


class BaseObjectModel(Model):
    id = fields.IntField(pk=True)
    uid = fields.BigIntField(description="Telegram unique identifier")
    name = fields.CharField(max_length=128, description="Name from telegram: Fullname or Title")
    created_at = fields.DatetimeField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
