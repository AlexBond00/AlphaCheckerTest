from tortoise import fields
from tortoise.models import Model


class User(Model):
    """User model."""
    id = fields.SmallIntField(pk=True)
    uid = fields.BigIntField()
    # Username to filter via admin interface in django
    username = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        schema = "inspector"
        table = 'user'
        table_description = "User description"


class GetInfoInspector(Model):
    id = fields.IntField(pk=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "inspector.User",
        on_delete=fields.CASCADE,
        related_name="info"
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        schema = "inspector"
        table = "get_info_inspector"
        table_description = "Statistics the inspector"


class UpdateInspector(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "inspector.User",
        on_delete=fields.CASCADE,
        related_name="updates"
    )
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        schema = "inspector"
        table = "update_inspector"
        table_description = "Statistics the inspector"


class FoundClientByInspector(Model):
    id = fields.IntField(pk=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        model_name="inspector.User",
        on_delete=fields.CASCADE,
        related_name="clients"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    channel_id = fields.IntField(description="Channel uid(-102932939)")

    class Meta:
        schema = "inspector"
        table = "found_client_by_inspector"
        table_description = "Statistics the inspector"
