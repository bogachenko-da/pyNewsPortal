# Generated by Django 4.2.5 on 2023-10-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(choices=[('AR', 'Статья'), ('NW', 'Новость')], default='NW', max_length=2),
        ),
    ]