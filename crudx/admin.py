from django.contrib import admin
from .models import StudentsData,RandomWord,images,testing


class ShowId(admin.ModelAdmin):
  readonly_fields= (["id"])

admin.site.register(StudentsData,ShowId)
admin.site.register(RandomWord,ShowId)
admin.site.register(images,ShowId)
admin.site.register(testing,ShowId)
