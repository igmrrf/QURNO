# Generated by Django 4.0.5 on 2022-06-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(max_length=225, verbose_name='پیام'),
        ),
    ]
