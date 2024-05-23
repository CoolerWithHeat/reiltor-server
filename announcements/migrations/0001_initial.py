# Generated by Django 5.0.4 on 2024-05-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('images', models.FileField(default=None, upload_to='')),
                ('square_meters', models.FloatField()),
                ('floor', models.IntegerField()),
                ('bathroom', models.CharField(choices=[('Раздельный', 'Раздельный'), ('Совмещенный', 'Совмещенный')], default='Раздельный', max_length=100)),
                ('room_count', models.IntegerField()),
                ('construction_material', models.CharField(choices=[('Кирпичный', 'Кирпичный'), ('Панельный', 'Панельный'), ('Монолитный', 'Монолитный')], default='Раздельное', max_length=100)),
                ('landmark', models.CharField(max_length=100, verbose_name='Orentir')),
                ('room_layout', models.CharField(choices=[('Раздельное', 'Раздельное'), ('Cмежные', 'Cмежные'), ('Cмежные-раздельные', 'Cмежные-раздельные')], default='Раздельное', max_length=100, verbose_name='Planirovka')),
                ('end_wall_structure', models.BooleanField(default=False, verbose_name='Torets')),
                ('mortgage_deal_possible', models.BooleanField(default=False, verbose_name='Ipoteka')),
            ],
        ),
    ]
