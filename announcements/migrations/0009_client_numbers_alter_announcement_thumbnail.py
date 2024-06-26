# Generated by Django 5.0.6 on 2024-05-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0008_remove_announcement_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='+998', max_length=18, verbose_name='вторичный номер')),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='thumbnail',
            field=models.FileField(default='Any Picture', upload_to='', verbose_name='миниатюра'),
        ),
    ]
