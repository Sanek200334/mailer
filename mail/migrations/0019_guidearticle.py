# Generated by Django 2.2.4 on 2020-04-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0018_customuser_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('text', models.TextField(null=True)),
                ('image', models.FileField(upload_to='media/images')),
            ],
        ),
    ]