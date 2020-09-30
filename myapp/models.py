from django.db import models


# Create your models here.
class InvitationCode(models.Model):
    code = models.CharField(verbose_name="邀请码", max_length=10, unique=True)
    expire = models.DateTimeField(verbose_name="过期时间")

    def __str__(self):
        return self.code



