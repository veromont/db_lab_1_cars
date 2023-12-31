# Generated by Django 4.2.6 on 2023-10-21 10:26

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=16384)),
            ],
            options={
                'db_table': 'articles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('max_speed', models.FloatField()),
                ('transmission', models.IntegerField(choices=[(1, 'Manual'), (2, 'Semi-automatic'), (3, 'Automatic')], default=1)),
            ],
            options={
                'db_table': 'car_models',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CarRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vin', models.CharField(db_column='VIN', max_length=17, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('color_hex', models.CharField(max_length=7)),
                ('assemble_year', models.IntegerField()),
                ('estimated_value', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 13, 26, 44, 867679), editable=False)),
                ('verified_by_dealership', models.IntegerField(blank=True, null=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Not verified'), (2, 'Verified'), (3, 'Archived')], default=1)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.carmodel')),
            ],
            options={
                'db_table': 'car_records',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('bio', models.CharField(blank=True, max_length=512, null=True)),
                ('birth_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'dealers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'dealerships',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DealReview',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('content', models.CharField(blank=True, max_length=4096, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 13, 26, 44, 868684), editable=False)),
            ],
            options={
                'db_table': 'deal_reviews',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('country', models.IntegerField(choices=[(1, 'Ukraine'), (2, 'Poland'), (3, 'Not specified')], default=3)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'regions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'tags',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_admin', models.BooleanField()),
                ('name', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('registration_date', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 13, 26, 44, 870684), editable=False)),
                ('credit_score', models.IntegerField(blank=True, null=True)),
                ('region', models.ForeignKey(default='UKRAINE', on_delete=django.db.models.deletion.SET_DEFAULT, to='lab.region')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('logo', django.contrib.postgres.fields.ArrayField(base_field=models.BinaryField(), blank=True, null=True, size=None)),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.tag')),
            ],
            options={
                'db_table': 'makers',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_id', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 13, 26, 44, 869684), editable=False)),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.tag')),
            ],
            options={
                'db_table': 'features',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DealerWorkHistoryRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('works_from', models.DateTimeField()),
                ('terminated_at', models.DateTimeField(blank=True, null=True)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.dealer')),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.dealership')),
            ],
            options={
                'db_table': 'dealer_work_history_records',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='dealership',
            name='maker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.maker'),
        ),
        migrations.AddField(
            model_name='dealership',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.region'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='dealership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.dealership'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.user'),
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Available'), (2, 'Not available'), (3, 'Closed')], default=1)),
                ('price', models.FloatField()),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 13, 26, 44, 869684))),
                ('updated_by_user', models.IntegerField()),
                ('car_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.carrecord')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.user')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.dealer')),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.dealreview')),
            ],
            options={
                'db_table': 'deals',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='carrecord',
            name='created_by_dealer',
            field=models.ForeignKey(db_column='created_by_dealer', on_delete=django.db.models.deletion.DO_NOTHING, to='lab.dealer'),
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', django.contrib.postgres.fields.ArrayField(base_field=models.BinaryField(), size=None)),
                ('car_record', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.carrecord')),
            ],
            options={
                'db_table': 'car_photos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='carmodel',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.maker'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lab.tag'),
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.tag')),
            ],
            options={
                'db_table': 'article_tags',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.user'),
        ),
        migrations.CreateModel(
            name='FeaturesCarRecord',
            fields=[
                ('features', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='lab.feature')),
                ('car_records', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lab.carrecord')),
            ],
            options={
                'db_table': 'features_car_records',
                'managed': True,
            },
        ),
    ]
