# Generated by Django 2.2.4 on 2019-10-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0005_auto_20191016_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
