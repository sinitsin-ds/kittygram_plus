# Generated by Django 3.2 on 2023-05-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20230517_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]
