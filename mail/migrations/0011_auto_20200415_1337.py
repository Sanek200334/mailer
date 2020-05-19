# Generated by Django 2.2.4 on 2020-04-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0010_auto_20200329_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('summ', models.CharField(max_length=8)),
                ('status', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='htmlsend',
            name='our_file',
            field=models.FileField(upload_to='../mailer.su/sender/mail/templates/sending-templates'),
        ),
    ]