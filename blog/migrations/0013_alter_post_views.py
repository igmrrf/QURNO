# Generated by Django 4.0.5 on 2022-07-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveBigIntegerField(blank=True, default=0, verbose_name='بازدید ها'),
        ),
    ]
