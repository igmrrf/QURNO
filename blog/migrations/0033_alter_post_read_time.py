# Generated by Django 4.0.6 on 2022-07-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='read_time',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='مدت زمان مورد نیاز برای مطالعه'),
        ),
    ]
