# Generated by Django 4.0.6 on 2022-07-19 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0034_category_designer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='designer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blog_categories', to=settings.AUTH_USER_MODEL, verbose_name='طراح دسته بندی'),
        ),
    ]