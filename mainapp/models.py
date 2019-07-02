from django.db.models import Model
from django.db import models
from django.shortcuts import reverse

from autoslug import AutoSlugField

from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Դուք կարող եք ստեղծել միայն մեկ" % model.__name__)






class Header(models.Model):
    title_1_hy = models.CharField(max_length=20, db_index=True, verbose_name='Հարցազրույցներ:')
    title_1_ru = models.CharField(max_length=20, db_index=True, verbose_name='Интервью:')
    title_1_en = models.CharField(max_length=20, db_index=True, verbose_name='Interviews:')
    title_2_hy = models.CharField(max_length=20, db_index=True, verbose_name='Ծրագրեր:')
    title_2_ru = models.CharField(max_length=20, db_index=True, verbose_name='Программы:')
    title_2_en = models.CharField(max_length=20, db_index=True, verbose_name='Programs:')
    title_3_hy = models.CharField(max_length=20, db_index=True, verbose_name='Հաղորդացանց:')
    title_3_ru = models.CharField(max_length=20, db_index=True, verbose_name='Трансляций:')
    title_3_en = models.CharField(max_length=20, db_index=True, verbose_name='Broadcasts:')
    title_4_hy = models.CharField(max_length=20, db_index=True, verbose_name='Բլոգ:')
    title_4_ru = models.CharField(max_length=20, db_index=True, verbose_name='Блог:')
    title_4_en = models.CharField(max_length=20, db_index=True, verbose_name='Blog:')
    title_5_hy = models.CharField(max_length=20, db_index=True, verbose_name='Մեր մասին:')
    title_5_ru = models.CharField(max_length=20, db_index=True, verbose_name='О нас:')
    title_5_en = models.CharField(max_length=20, db_index=True, verbose_name='About us:')
    listen_url = models.CharField(max_length=500, db_index=True, verbose_name='Լսելու Լինք:')
    watch_url = models.CharField(max_length=500, db_index=True, verbose_name='Դիտելու Լինք:')

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Ցանկի կետերը'


class Slider(models.Model):
    image = models.ImageField(upload_to='slider/%Y/%m/%d/', blank=True, verbose_name='Նկար:')


    class Meta:
        verbose_name_plural = 'Սլայդերի նկարներ'




class GeneralPicture(models.Model):
    general_picture = models.ImageField(upload_to='general/%Y/%m/%d/', blank=True, verbose_name='Նկար:')

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Գլխավոր էջի նկար'


class GeneralVid(models.Model):
    yt_url = models.CharField(max_length=1000, db_index=True, verbose_name='YT URL:')

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Գլխավոր էջի տեսահոլովակ'


class GeneralVideos(models.Model):
    url_1 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    url_2 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    url_3 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    url_4 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')

    def clean(self):
        validate_only_one_instance(self)



    class Meta:
        verbose_name_plural = 'Գլխավոր էջի տեսահոլովակներ'


class TopNews(models.Model):
    title_hy = models.CharField(max_length=660, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=660, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=660, db_index=True, verbose_name='Title:')
    body_hy = models.TextField(max_length=660, db_index=True, verbose_name='Մարմին:')
    body_ru = models.TextField(max_length=660, db_index=True, verbose_name='Тело:')
    body_en = models.TextField(max_length=660, db_index=True, verbose_name='Body:')
    slug = AutoSlugField(populate_from='title_en', always_update=True, unique=True)
    image = models.ImageField(upload_to='topnews/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')


    class Meta:
        verbose_name_plural = 'Թոփ նորություններ'






class Interview(models.Model):
    title_hy = models.CharField(max_length=300, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=300, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=300, db_index=True, verbose_name='Title:')
    body_hy = models.TextField(max_length=300, blank=True, db_index=True, verbose_name='Մարմին:')
    body_ru = models.TextField(max_length=300, blank=True, db_index=True, verbose_name='Тело:')
    body_en = models.TextField(max_length=300, blank=True, db_index=True, verbose_name='Body:')
    slug = AutoSlugField(populate_from='title_en', always_update=True, unique=True)
    image = models.ImageField(upload_to='interviews/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_hy

    class Meta:
        verbose_name_plural = 'Հարցազրույցներ'
        ordering = ['-date_pub']



class Partners(models.Model):
    image_1 = models.ImageField(upload_to='partners/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url_1 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    image_2 = models.ImageField(upload_to='partners/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url_2 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    image_3 = models.ImageField(upload_to='partners/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url_3 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')
    image_4 = models.ImageField(upload_to='partners/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    url_4 = models.CharField(max_length=500, db_index=True, verbose_name='Լինք:')

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Գործընկերոջ նկար և լինք'



class Programs(models.Model):
    program_name_hy = models.CharField(max_length=200, db_index=True, verbose_name='Ծրագրի անուն:')
    program_name_ru = models.CharField(max_length=200, db_index=True, verbose_name='Имя программы:')
    program_name_en = models.CharField(max_length=200, db_index=True, verbose_name='Programm name:')
    title_hy = models.CharField(max_length=300, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=300, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=300, db_index=True, verbose_name='Title:')
    slug = AutoSlugField(populate_from='title_en', always_update=True, unique=True)
    author_hy = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Հեղինակ:')
    author_ru = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Автор:')
    author_en = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Author:')
    body_hy = models.TextField(blank=True, db_index=True, verbose_name='Մարմին:')
    body_ru = models.TextField(blank=True, db_index=True, verbose_name='Тело:')
    body_en = models.TextField(blank=True, db_index=True, verbose_name='Body:')
    image = models.ImageField(upload_to='programs/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title_hy

    class Meta:
        verbose_name_plural = 'Ծրագրեր'
        ordering = ['-date_pub']


class Broadcast(models.Model):
    week_dey_hy = models.CharField(max_length=150, db_index=True, verbose_name='Շաբաթվա օրը:')
    week_dey_ru = models.CharField(max_length=150, db_index=True, verbose_name='День недели:')
    week_dey_en = models.CharField(max_length=150, db_index=True, verbose_name='The day of the week:')
    date_hy = models.CharField(max_length=150, db_index=True, verbose_name='Ամսաթիվը:')
    date_ru = models.CharField(max_length=150, db_index=True, verbose_name='Дата:')
    date_en = models.CharField(max_length=150, db_index=True, verbose_name='Date:')
    title_hy = models.CharField(max_length=300, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=300, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=300, db_index=True, verbose_name='Title:')
    slug = AutoSlugField(populate_from='title_en', always_update=True, unique=True)
    from_time = models.TimeField(auto_now_add=False, verbose_name='Սկիզբը:')
    to_time = models.TimeField(auto_now_add=False, verbose_name='Ավարտը:')
    image = models.ImageField(upload_to='broadcasts/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Հաղորդացանցեր'
        ordering = ['date_pub']




class Blog(models.Model):
    program_name_hy = models.CharField(max_length=200, db_index=True, verbose_name='Ծրագրի անուն:')
    program_name_ru = models.CharField(max_length=200, db_index=True, verbose_name='Имя программы:')
    program_name_en = models.CharField(max_length=200, db_index=True, verbose_name='Programm name:')
    title_hy = models.CharField(max_length=300, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=300, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=300, db_index=True, verbose_name='Title:')
    slug = AutoSlugField(populate_from='title_en', always_update=True, unique=True)
    author_hy = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Հեղինակ:')
    author_ru = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Автор:')
    author_en = models.CharField(max_length=50, blank=True, db_index=True, verbose_name='Author:')
    body_hy = models.TextField(blank=True, db_index=True, verbose_name='Մարմին:')
    body_ru = models.TextField(blank=True, db_index=True, verbose_name='Тело:')
    body_en = models.TextField(blank=True, db_index=True, verbose_name='Body:')
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, verbose_name='Նկար:')
    date_pub = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Բլոգ'



class Ourme(models.Model):
    title_hy = models.CharField(max_length=150, db_index=True, verbose_name='Վերնագիր:')
    title_ru = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок:')
    title_en = models.CharField(max_length=150, db_index=True, verbose_name='Title:')
    body_hy = models.TextField(max_length=20000, db_index=True, verbose_name='Մարմին:')
    body_ru = models.TextField(max_length=20000, db_index=True, verbose_name='Тело:')
    body_en = models.TextField(max_length=20000, db_index=True, verbose_name='Body:')
    image = models.ImageField(upload_to='ourme/%Y/%m/%d/', blank=True, verbose_name='Նկար:')

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Մեր մասին'



class Footer(models.Model):
    appstore_url = models.CharField(max_length=500, db_index=True, verbose_name='App Store-ի Լինք:')
    playmarket_url = models.CharField(max_length=500, db_index=True, verbose_name='Play Market-ի Լինք:')
    facebook = models.CharField(max_length=500, db_index=True, verbose_name='Facebook:')
    yuotube = models.CharField(max_length=500, db_index=True, verbose_name='YouTube:')
    soundcloud = models.CharField(max_length=500, db_index=True, verbose_name='SoundCloud:')
    text_hy = models.TextField(max_length=530, db_index=True, verbose_name='© Տեքստ:')
    text_ru = models.TextField(max_length=530, db_index=True, verbose_name='© Текст:')
    text_en = models.TextField(max_length=530, db_index=True, verbose_name='© Text:')
    year = models.DateField(auto_now=True)

    def clean(self):
        validate_only_one_instance(self)

    class Meta:
        verbose_name_plural = 'Վերջաբան'





