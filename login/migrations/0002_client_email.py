# Generated by Django 2.0.2 on 2018-04-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.TextField(default='abc@xyz.com', max_length=100),
        ),
    ]
