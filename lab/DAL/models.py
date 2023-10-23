import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models


class ArticleTag(models.Model):
    tag = models.ForeignKey('Tag', models.CASCADE)
    article = models.ForeignKey('Article', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'article_tags'
        app_label = "lab"


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=16384)
    author = models.ForeignKey('User', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'articles'
        app_label = "lab"

    def __str__(self):
        return self.title


class CarModel(models.Model):
    MANUAL = 1
    SEMI = 2
    AUTO = 3
    STATUS_CHOICES = (
        (MANUAL, 'Manual'),
        (SEMI, 'Semi-automatic'),
        (AUTO, 'Automatic'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    max_speed = models.FloatField()
    transmission = models.IntegerField(choices=STATUS_CHOICES, default=MANUAL)
    maker = models.ForeignKey('Maker', models.DO_NOTHING)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'car_models'
        app_label = "lab"

    def __str__(self):
        return self.name


class CarPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    car_record = models.ForeignKey('CarRecord', models.DO_NOTHING)
    content = ArrayField(
        models.BinaryField(),
    )

    class Meta:
        managed = True
        db_table = 'car_photos'
        app_label = "lab"


class CarRecord(models.Model):
    NOT_VERIFIED = 1
    VERIFIED = 2
    ARCHIVED = 3
    STATUS_CHOICES = (
        (NOT_VERIFIED, 'Not verified'),
        (VERIFIED, 'Verified'),
        (ARCHIVED, 'Archived'),
    )

    id = models.IntegerField(primary_key=True)
    vin = models.CharField(db_column='vin', max_length=17)
    name = models.CharField(max_length=64)
    car_model = models.ForeignKey(CarModel, models.DO_NOTHING)
    color_hex = models.CharField(max_length=7)
    assemble_year = models.IntegerField()
    estimated_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    created_by_dealer = models.ForeignKey('Dealer', models.DO_NOTHING, db_column='created_by_dealer')
    verified_by_dealership = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOT_VERIFIED)

    class Meta:
        managed = True
        db_table = 'car_records'
        app_label = "lab"

    def __str__(self):
        return self.name.__str__()


class DealReview(models.Model):
    id = models.IntegerField(primary_key=True)
    rating = models.IntegerField()
    content = models.CharField(max_length=4096, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    class Meta:
        managed = True
        db_table = 'deal_reviews'
        app_label = "lab"


class DealerWorkHistoryRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    dealer = models.ForeignKey('Dealer', models.DO_NOTHING)
    dealership = models.ForeignKey('Dealership', models.CASCADE)
    works_from = models.DateTimeField()
    terminated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dealer_work_history_records'
        app_label = "lab"


class Dealer(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    number = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    bio = models.CharField(max_length=512, blank=True, null=True)
    dealership = models.ForeignKey('Dealership', models.DO_NOTHING, blank=True, null=True)
    birth_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'dealers'
        app_label = "lab"

    def __str__(self):
        return self.user.__str__()


class Dealership(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    maker = models.ForeignKey('Maker', models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=128)
    region = models.ForeignKey('Region', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'dealerships'
        app_label = "lab"


class Deal(models.Model):
    CREATED = 1
    DONE = 2
    CLOSED = 3
    STATUS_CHOICES = (
        (CREATED, "Available"),
        (DONE, "Not available"),
        (CLOSED, "Closed"),
    )

    id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    dealer = models.ForeignKey(Dealer, models.DO_NOTHING)
    car_record = models.ForeignKey(CarRecord, models.DO_NOTHING)
    review = models.ForeignKey(DealReview, models.DO_NOTHING, blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=CREATED,
    )

    price = models.FloatField()
    updated_at = models.DateTimeField(default=datetime.datetime.now())
    updated_by_user = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'deals'
        app_label = "lab"


class Feature(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=64)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    class Meta:
        managed = True
        db_table = 'features'
        app_label = "lab"


class FeaturesCarRecord(models.Model):
    features = models.OneToOneField(Feature, models.DO_NOTHING, primary_key=True)
    car_records = models.ForeignKey(CarRecord, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'features_car_records'
        app_label = "lab"


class Maker(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True, null=True)
    logo = ArrayField(
        models.BinaryField(),
        null=True,
        blank=True,
    )
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'makers'
        app_label = "lab"

    def __str__(self):
        return self.name


class Region(models.Model):
    UKRAINE = 1
    POLAND = 2
    OTHER = 3
    COUNTRY_CHOICES = (
        (UKRAINE, 'Ukraine'),
        (POLAND, 'Poland'),
        (OTHER, 'Not specified'),
    )

    id = models.IntegerField(primary_key=True)
    country = models.IntegerField(choices=COUNTRY_CHOICES, default=OTHER)
    name = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'regions'
        app_label = "lab"

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'tags'
        app_label = "lab"

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    is_admin = models.BooleanField()
    name = models.CharField(max_length=64)
    username = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64)
    registration_date = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    credit_score = models.IntegerField(blank=True, null=True)
    region = models.ForeignKey(Region, models.SET_DEFAULT, default='UKRAINE')

    class Meta:
        managed = True
        db_table = 'users'
        app_label = "lab"

    def __str__(self):
        return self.username
