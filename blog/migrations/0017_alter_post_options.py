# Generated by Django 4.0.5 on 2022-07-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-datetime_created',), 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
    ]
