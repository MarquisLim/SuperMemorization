# Generated by Django 4.1.7 on 2023-04-03 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='decks', to=settings.AUTH_USER_MODEL),
        ),
    ]
