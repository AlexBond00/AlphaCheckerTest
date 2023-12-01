from django.db import models


class CheckerUser(models.Model):
    """User model for checker."""
    uid = models.BigIntegerField()
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inspector"."user'

    def __str__(self):
        return self.username


class GetInfoInspector(models.Model):
    """Model that represents every '/getinfo' by User (inspector)."""
    user = models.ForeignKey(
        CheckerUser,
        on_delete=models.CASCADE,
        related_name="info"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inspector"."get_info_inspector'


class UpdateInspector(models.Model):
    """Model that represents every successful '/update' by User (inspector)."""
    user = models.ForeignKey(
        CheckerUser,
        on_delete=models.CASCADE,
        related_name="updates"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inspector"."update_inspector'


class FoundClientByInspector(models.Model):
    """Model that represents every successful tg user found in channel."""
    user = models.ForeignKey(
        CheckerUser,
        on_delete=models.CASCADE,
        related_name="clients"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    channel_id = models.IntegerField()

    class Meta:
        db_table = 'inspector"."found_client_by_inspector'
