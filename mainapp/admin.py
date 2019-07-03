from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *



class HeaderAdmin(SummernoteModelAdmin):
    list_display = ['title_1_hy', 'title_1_ru', 'title_1_en',
                    'title_2_hy', 'title_2_ru', 'title_2_en',
                    'title_3_hy', 'title_3_ru', 'title_3_en',
                    'title_4_hy', 'title_4_ru', 'title_4_en',
                    'title_5_hy', 'title_5_ru', 'title_5_en',
                    'listen_url', 'watch_url']
    summernote_fields = '__all__'


class SliderAdmin(SummernoteModelAdmin):
    list_display = ['image']
    summernote_fields = '__all__'


class GeneralPictureAdmin(SummernoteModelAdmin):
    list_display = ['general_picture']
    summernote_fields = '__all__'

class GeneralVidAdmin(SummernoteModelAdmin):
    list_display = ['yt_url']
    summernote_fields = '__all__'


class GeneralVideosAdmin(SummernoteModelAdmin):
    list_display = ['url_1', 'url_2', 'url_3', 'url_4', ]
    summernote_fields = '__all__'


class TopNewsAdmin(SummernoteModelAdmin):
    list_display = ['title_hy', 'title_ru', 'title_en',
                    'body_hy', 'body_ru', 'body_en',
                    'url']
    summernote_fields = '__all__'


class PartnersAdmin(SummernoteModelAdmin):
    # list_display = ['url_1', 'url_2', 'url_3', 'url_4']
    summernote_fields = '__all__'



class InterviewAdmin(SummernoteModelAdmin):
    list_display = ['title_hy', 'title_ru', 'title_en',
                    'body_hy', 'body_ru', 'body_en',
                    'url']
    summernote_fields = '__all__'

class BroadcastDateAdmin(SummernoteModelAdmin):
    list_display = ['week_dey_hy', 'week_dey_ru', 'week_dey_en',
                    'date_hy', 'date_ru',  'date_en']
    summernote_fields = '__all__'

class ProgramsAdmin(SummernoteModelAdmin):
    list_display = ['title_hy', 'title_ru', 'title_en',
                    'author_hy', 'author_ru', 'author_en',
                    'slug']
    summernote_fields = '__all__'

class BroadcastAdmin(SummernoteModelAdmin):
    list_display = ['title_hy', 'title_ru', 'title_en',
                    'slug', 'from_time', 'to_time']
    summernote_fields = '__all__'


class BlogAdmin(SummernoteModelAdmin):
    list_display = ['title_hy', 'title_ru', 'title_en',
                    'author_hy', 'author_ru', 'author_en',
                    'slug']
    summernote_fields = '__all__'


class AboutUsAdmin(SummernoteModelAdmin):
    list_display = ['body_hy', 'body_ru', 'body_en']
    summernote_fields = '__all__'


class FooterAdmin(SummernoteModelAdmin):
    list_display = ['appstore_url', 'playmarket_url', 'facebook', 'yuotube', 'soundcloud']



admin.site.register(Header, HeaderAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(GeneralPicture, GeneralPictureAdmin)
admin.site.register(GeneralVid, GeneralVidAdmin)
admin.site.register(GeneralVideos, GeneralVideosAdmin)
admin.site.register(TopNews, TopNewsAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Programs, ProgramsAdmin)
admin.site.register(BroadcastDate, BroadcastDateAdmin)
admin.site.register(Broadcast, BroadcastAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Footer, FooterAdmin)


