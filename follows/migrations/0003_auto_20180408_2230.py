# Generated by Django 2.0.2 on 2018-04-08 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follows', '0002_auto_20180408_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
