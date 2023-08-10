from django.contrib import admin

from .models import Answer
from .models import Profile
from .models import Job
from .models import ChatMessage

admin.site.register(Profile)
admin.site.register(Answer)
admin.site.register(Job)
admin.site.register(ChatMessage)
