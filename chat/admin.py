from django.contrib import admin

from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    field = ("chat", "text", 'created_at', 'author', 'reciever')
    list_display = ("chat", "text", 'created_at', 'author', 'receiver')
    search_fields = ('text',)

# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)