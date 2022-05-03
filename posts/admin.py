from django.contrib import admin

# Register your models here. pass admin2 - ciscocisco
from .models import User
from .models import Posts
from .models import Categories
from .models import Posts2
from .models import RegUser

admin.site.register(RegUser)
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Posts2)
