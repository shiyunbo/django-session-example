from django.contrib import admin
from .models import InvitationCode


# Register your models here.
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "expire")

    class Meta:
        model = InvitationCode


admin.site.register(InvitationCode, InvitationCodeAdmin)