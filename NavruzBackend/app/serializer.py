from rest_framework import serializers
from .models import ImageModel, AppUser, TrashBin

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"

class TrashBinSerializer(serializers.ModelSerializer):
    added_by = AppUserSerializer()
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=ImageModel.objects.all())

    class Meta:
        model = TrashBin
        fields = "__all__"
