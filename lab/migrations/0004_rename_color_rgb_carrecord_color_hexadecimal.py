# Generated by Django 4.2.6 on 2023-10-20 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_rename_volume_engine_carmodel_max_speed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrecord',
            old_name='color_rgb',
            new_name='color_hexadecimal',
        ),
    ]
