# Generated by Django 4.2.6 on 2023-10-20 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_rename_color_rgb_carrecord_color_hexadecimal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrecord',
            old_name='color_hexadecimal',
            new_name='color_hex',
        ),
        migrations.AlterField(
            model_name='carrecord',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 22, 36, 47, 318996), editable=False),
        ),
        migrations.AlterField(
            model_name='deal',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 22, 36, 47, 319996)),
        ),
        migrations.AlterField(
            model_name='dealreview',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 22, 36, 47, 318996), editable=False),
        ),
        migrations.AlterField(
            model_name='feature',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 22, 36, 47, 320996), editable=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 22, 36, 47, 321999), editable=False),
        ),
    ]
