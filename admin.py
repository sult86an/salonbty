from django.contrib import admin
from .models import Days, Hours, Salons, Orders, Services, Artists, Tasks,  Member, Hotel, Offers, WorkDays, BreakHours


admin.site.register(Days)
admin.site.register(Hours)
admin.site.register(Salons)
admin.site.register(Orders)
admin.site.register(Services)
admin.site.register(Artists)
# admin.site.register(ArtistServices)
admin.site.register(Tasks)

admin.site.register(Member)
admin.site.register(Hotel)
admin.site.register(Offers)
admin.site.register(WorkDays)
admin.site.register(BreakHours)

