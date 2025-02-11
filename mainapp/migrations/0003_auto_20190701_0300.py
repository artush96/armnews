# Generated by Django 2.2.2 on 2019-06-30 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190701_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_picture', models.ImageField(blank=True, upload_to='general/%Y/%m/%d/', verbose_name='Նկար:')),
            ],
            options={
                'verbose_name_plural': 'Գլխավոր էջի նկար',
            },
        ),
        migrations.CreateModel(
            name='GeneralVid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_url', models.CharField(db_index=True, max_length=1000, verbose_name='YT URL:')),
            ],
            options={
                'verbose_name_plural': 'Գլխավոր էջի տեսահոլովակ',
            },
        ),
        migrations.DeleteModel(
            name='General',
        ),
    ]
