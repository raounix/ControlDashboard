from django.contrib import admin
from .models import Server,SSW,SSWConfig,SBC,SBCConfig
# Register your models here.




admin.site.register(Server)
admin.site.register(SSW)
admin.site.register(SSWConfig)
admin.site.register(SBC)
admin.site.register(SBCConfig)