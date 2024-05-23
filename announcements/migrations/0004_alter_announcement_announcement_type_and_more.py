# Generated by Django 5.0.6 on 2024-05-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_announcement_announcement_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announcement_type',
            field=models.CharField(choices=[('продается', 'продается'), ('в аренду', 'в аренду')], default='продается', max_length=35, verbose_name='объявление'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='apartment_region',
            field=models.CharField(choices=[('Чиланзар', 'Чиланзар'), ('Мирабад', 'Мирабад'), ('Сергели', 'Сергели'), ('Учтепинский', 'Учтепинский'), ('Бектемир', 'Бектемир'), ('Мирзо-Улугбек', 'Мирзо-Улугбек'), ('Шайхантаур', 'Шайхантаур'), ('Юнусабад', 'Юнусабад'), ('Яккасарай', 'Яккасарай'), ('Яшнабад', 'Яшнабад'), ('Алмазар', 'Алмазар')], default='Чиланзар', max_length=35, verbose_name='район'),
        ),
        migrations.AlterField(
            model_name='phone_number',
            name='number',
            field=models.CharField(default='+998997010098', max_length=18, verbose_name='вторичный номер'),
        ),
        migrations.AlterField(
            model_name='reiltor_number',
            name='main_reiltor_number',
            field=models.CharField(default='+998997010098', max_length=18, verbose_name='Основной номер'),
        ),
    ]
