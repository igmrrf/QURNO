# Generated by Django 4.0.6 on 2022-07-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False, verbose_name='وضعیت فعال سازی'),
        ),
    ]
