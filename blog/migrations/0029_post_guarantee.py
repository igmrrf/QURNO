# Generated by Django 4.0.6 on 2022-07-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_comment_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='guarantee',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت ضمانت'),
        ),
    ]
