# Generated by Django 2.2.4 on 2020-03-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_customuser_active_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='htmlsend',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
