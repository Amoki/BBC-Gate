from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=32, help_text="The digicode")
    expires_at = models.DateTimeField(
        blank=True, null=True, help_text="The expiration date if needed"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="A short description of why this code has been created",
    )


class Rfid(models.Model):
    rfid_id = models.CharField(max_length=128, unique=True)
