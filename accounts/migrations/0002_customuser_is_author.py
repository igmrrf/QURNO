# Generated by Django 4.0.5 on 2022-06-26 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='وضعیت نویسندگی'),
        ),
    ]
