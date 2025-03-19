from rest_framework import serializers
from .models import ImageModel, AppUser, TrashBin, BinCategory

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = "__all__"


class BinCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BinCategory
        fields = "__all__"



class TrashBinSerializer(serializers.ModelSerializer):
    added_by = AppUserSerializer()
    images = ImageModelSerializer(many=True)
    categories = BinCategorySerializer(many=True)

    class Meta:
        model = TrashBin
        fields = "__all__"

    def create(self, validated_data):
        # Extract nested data for related fields.
        added_by_data = validated_data.pop('added_by', None)
        images_data = validated_data.pop('images', [])
        categories_data = validated_data.pop('categories', [])

        # Create the main TrashBin object.
        trash_bin = TrashBin.objects.create(**validated_data)

        # Process the nested user data.
        if added_by_data:
            # You can choose to either create a new user or look up an existing one.
            user, _ = AppUser.objects.get_or_create(**added_by_data)
            trash_bin.added_by = user
            trash_bin.save()

        # Process images.
        for image_data in images_data:
            image = ImageModel.objects.create(**image_data)
            trash_bin.images.add(image)

        # Process categories.
        for category_data in categories_data:
            category, _ = BinCategory.objects.get_or_create(**category_data)
            trash_bin.categories.add(category)

        return trash_bin

