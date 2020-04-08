# Generated by Django 2.2.4 on 2020-03-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0009_customuser_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='emails_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='messages_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twilio_account_sid',
            field=models.CharField(default='ACe449eb9c1ecabf1b928b78018404694d', max_length=60),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twilio_auth_token',
            field=models.CharField(default='9d32bd3cee9faf93dab5038bb837cae5', max_length=60),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twilio_phone_number',
            field=models.CharField(default='+12568343892', max_length=30),
        ),
    ]
