from django.contrib import admin

# Register your models here.
from store.models import *
admin.site.register(Book)
admin.site.register(Mug)
admin.site.register(MugImg)
admin.site.register(Tshirt)
admin.site.register(TshirtImg)
admin.site.register(Pc)
admin.site.register(PcImg)
admin.site.register(LapTop)
admin.site.register(LapTopImg)


