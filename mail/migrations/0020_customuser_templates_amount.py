# Generated by Django 2.2.4 on 2020-05-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0019_guidearticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='templates_amount',
            field=models.IntegerField(default=0),
        ),
    ]