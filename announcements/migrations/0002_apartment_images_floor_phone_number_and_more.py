# Generated by Django 5.0.6 on 2024-05-15 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='apartment_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default=None, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Apartment Images',
            },
        ),
        migrations.CreateModel(
            name='floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_total_floor', models.IntegerField(verbose_name='Этажность здания')),
                ('apartment_floor', models.IntegerField(default=None, verbose_name='этаж квартиры')),
                ('apartment_room_count', models.IntegerField(verbose_name='количество комнаты в квартире')),
            ],
        ),
        migrations.CreateModel(
            name='phone_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='+998997010098', max_length=15, verbose_name='вторичный номер')),
            ],
            options={
                'verbose_name_plural': 'сохраненные номеры',
            },
        ),
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name_plural': 'Announcements'},
        ),
        migrations.AddField(
            model_name='announcement',
            name='description',
            field=models.TextField(default='нет описания', max_length=620, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='kitchen_size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='метр.к кухня'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='kvartal',
            field=models.IntegerField(choices=[(0, '1-Квартал '), (1, '2-Квартал '), (2, '3-Квартал '), (3, '4-Квартал '), (4, '5-Квартал '), (5, '6-Квартал '), (6, '7-Квартал '), (7, '8-Квартал '), (8, '9-Квартал '), (9, '10-Квартал '), (10, '11-Квартал '), (11, '12-Квартал '), (12, '13-Квартал '), (13, '14-Квартал '), (14, '15-Квартал '), (15, '16-Квартал '), (16, '17-Квартал '), (17, '18-Квартал '), (18, '19-Квартал '), (19, '20-Квартал '), (20, '21-Квартал '), (21, '22-Квартал '), (22, '23-Квартал '), (23, '24-Квартал '), (24, '25-Квартал '), (25, '26-Квартал '), (26, '27-Квартал (Алгоритм)'), (27, '28-Квартал (Алгоритм)'), (28, '29-Квартал (Алгоритм)'), (29, '30-Квартал (Алгоритм)'), (30, '31-Квартал (Алгоритм)'), (31, 'Наккошлик'), (32, 'Думбрабод'), (33, 'Квартал Г9а'), (34, 'Квартал Ц'), (35, 'Квартал Е'), (36, 'Квартал И')], default=20, verbose_name='Квартал'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='thumbnail',
            field=models.FileField(default='Any Picture', upload_to=''),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='bathroom',
            field=models.CharField(choices=[('Раздельный', 'Раздельный'), ('Совмещенный', 'Совмещенный')], default='Раздельный', max_length=100, verbose_name='структура санузеля'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='construction_material',
            field=models.CharField(choices=[('Кирпичный', 'Кирпичный'), ('Панельный', 'Панельный'), ('Монолитный', 'Монолитный')], default='Раздельное', max_length=100, verbose_name='Материал квартиры'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='end_wall_structure',
            field=models.BooleanField(default=False, verbose_name='Торец'),
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='images',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='landmark',
            field=models.CharField(max_length=100, verbose_name='Ориентир'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.CharField(max_length=100, verbose_name='расположение кв'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='mortgage_deal_possible',
            field=models.BooleanField(default=False, verbose_name='Ипотека'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='room_count',
            field=models.IntegerField(verbose_name='количество комнат'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='room_layout',
            field=models.CharField(choices=[('Раздельное', 'Раздельное'), ('Cмежные', 'Cмежные'), ('Cмежные-раздельные', 'Cмежные-раздельные')], default='Раздельное', max_length=100, verbose_name='Планировка'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='square_meters',
            field=models.FloatField(verbose_name='кв метр'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='заголовок'),
        ),
        migrations.CreateModel(
            name='announcement_recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_list', models.ManyToManyField(to='announcements.announcement', verbose_name='список рекомендаций')),
            ],
            options={
                'verbose_name_plural': 'Рекомендация',
            },
        ),
        migrations.AlterField(
            model_name='announcement',
            name='floor',
            field=models.OneToOneField(blank=True, default='Provider Data', null=True, on_delete=django.db.models.deletion.CASCADE, to='announcements.floor', verbose_name='этаж'),
        ),
        migrations.CreateModel(
            name='Reiltor_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reiltor_name', models.CharField(default='Масуд', max_length=25, verbose_name='имя риэлтора')),
                ('main_reiltor_number', models.CharField(default='+998997010098', max_length=15, verbose_name='Основной номер')),
                ('secondary_numbers', models.ManyToManyField(blank=True, to='announcements.phone_number', verbose_name='вторичный номер')),
            ],
            options={
                'verbose_name_plural': 'контакт риэлтора',
            },
        ),
        migrations.AddField(
            model_name='announcement',
            name='images',
            field=models.ManyToManyField(to='announcements.apartment_images', verbose_name='изображений кв'),
        ),
    ]