# Generated by Django 4.0.3 on 2022-04-29 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mealplans', '0002_alter_mealplan_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mealplans', to=settings.AUTH_USER_MODEL),
        ),
    ]
