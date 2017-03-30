from django.contrib.admin import ModelAdmin


class WebsiteAdmin(ModelAdmin):
    list_display = ('url', 'delay', 'response_code', 'response_time')

