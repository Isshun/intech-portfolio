from django.contrib import admin
from apps.main.models import File, Project, Skill, Timeline, Tag

#class ColorAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('name',       {'fields': ['name']}),
#        ('description',{'fields': ['description']}),
#    ]
#    search_fields = ['name']

admin.site.register(File)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Timeline)
admin.site.register(Tag)
