# Generated by Django 4.0.5 on 2022-07-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_category_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='defaults/blog_post_default_banner.png', upload_to='blog/post/', verbose_name='بنر'),
        ),
    ]
