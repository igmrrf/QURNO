# Generated by Django 4.0.6 on 2022-07-17 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_post_guarantee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='guarantee',
        ),
    ]
