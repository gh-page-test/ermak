# Generated by Django 3.1.4 on 2021-01-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uifooter',
            name='water_mark',
        ),
        migrations.AddField(
            model_name='uifooter',
            name='link_dev',
            field=models.CharField(default='#', max_length=64, verbose_name='Ссылка на разработчика'),
        ),
        migrations.AddField(
            model_name='uifooter',
            name='name_dev',
            field=models.CharField(default='', max_length=64, verbose_name='Имя разработчика'),
        ),
        migrations.AlterField(
            model_name='uifooter',
            name='email',
            field=models.CharField(default='', max_length=128, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='uifooter',
            name='tel',
            field=models.CharField(default='', max_length=14, verbose_name='Телефон'),
        ),
    ]
