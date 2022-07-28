# Generated by Django 4.0.5 on 2022-07-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=225, unique=True, verbose_name='توضیحات'),
        ),
    ]