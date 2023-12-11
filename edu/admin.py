from django.contrib import admin
from edu import models as m

# Register your models here.
admin.site.register(m.Settings)
admin.site.register(m.Portfolio)
admin.site.register(m.Work)
admin.site.register(m.Clients)
admin.site.register(m.Info)