# Generated by Django 3.1.4 on 2021-01-20 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('other_page', '0002_auto_20210120_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Ссылки на соц. сети', 'verbose_name_plural': 'Ссылки на соц. сети'},
        ),
        migrations.AddField(
            model_name='aboutme',
            name='inst',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page', to='other_page.social', verbose_name='Истаграм'),
        ),
    ]
