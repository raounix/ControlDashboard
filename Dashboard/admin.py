from django.contrib import admin
from .models import Server,SSW,SSW_SIPProfile,SBC,SBCConfig,RTP,RTPConfig
# Register your models here.




admin.site.register(Server)
admin.site.register(SSW)
admin.site.register(SSW_SIPProfile)
admin.site.register(SBC)
admin.site.register(SBCConfig)
admin.site.register(RTP)
admin.site.register(RTPConfig)