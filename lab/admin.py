from django.contrib import admin
from .DAL.models import *


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_speed', 'transmission']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author']


class CarRecordAdmin(admin.ModelAdmin):
    list_display = ['vin', 'name', 'car_model', 'color_hex',
                    'assemble_year', 'estimated_value', 'created_at', 'mileage', 'status']


class DealerAdmin(admin.ModelAdmin):
    list_display = ['user', 'number', 'email', 'bio', 'dealership', 'birth_date']


class DealAdmin(admin.ModelAdmin):
    list_display = ['customer', 'dealer', 'car_record', 'review', 'closed_at', 'status', 'price', 'updated_at']


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['type_id', 'description', 'name', 'created_at']


class MakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'logo']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['country', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_admin', 'name', 'username', 'password', 'registration_date', 'credit_score']


admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(CarRecord, CarRecordAdmin)
admin.site.register(Dealer, DealerAdmin)
admin.site.register(Deal, DealAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Maker, MakerAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(CarPhoto)
admin.site.register(DealReview)
admin.site.register(DealerWorkHistoryRecord)
admin.site.register(FeaturesCarRecord)
admin.site.register(ArticleTag)
