# Generated by Django 4.0.5 on 2022-06-26 00:12

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان ساخت')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='تاریخ و زمان آخرین تغییر')),
                ('active', models.BooleanField(default=True, verbose_name='فعال سا')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='blog/post/', verbose_name='بنر')),
                ('title', models.CharField(max_length=225, verbose_name='عنوان')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='محتوا')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='آخرین تغیر')),
                ('slug', models.SlugField(max_length=225, verbose_name='اسلاگ URL')),
                ('pub_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('read_time', models.PositiveSmallIntegerField(verbose_name='مدت زمان مورد نیاز برای مطالعه')),
                ('status', models.CharField(choices=[('0', 'پیش نویس'), ('1', 'منتشر شده')], default='0', max_length=225, verbose_name='وضعیت')),
                ('active', models.BooleanField(default=True, verbose_name='وضعیت فعال سازی')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_blog_posts', to='blog.category', verbose_name='دسته بندی')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]
