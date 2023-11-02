# Generated by Django 4.2.1 on 2023-11-02 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seotool', '0010_keywords_suggestion_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywords_suggestion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
