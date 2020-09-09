from django.contrib import admin

# Register your models here.
from .models import Bids
from .models import User

admin.site.register(Bids)
admin.site.register(User)
