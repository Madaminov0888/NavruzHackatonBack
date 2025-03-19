from django.contrib import admin
from .models import AppUser, ImageModel, TrashBin, BinCategory

@admin.register(AppUser)
class AdminAppUser(admin.ModelAdmin):
    list_display = ["name", "phone_number", "date_created"]

@admin.register(ImageModel)
class AdminImageModel(admin.ModelAdmin):
    list_display = ["id", "download_url", "storage_id", "date_created"]


@admin.register(BinCategory)
class AdminTrashBin(admin.ModelAdmin):
    list_display = ["id", "name", "date_created"]

@admin.register(TrashBin)
class AdminTrashBin(admin.ModelAdmin):
    list_display = ["id", "address", "added_by", "date_created"]
