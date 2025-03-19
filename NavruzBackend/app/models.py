from django.db import models
import uuid


class ImageModel(models.Model):
    id = models.CharField(max_length = 100, unique=True, primary_key=True, default=uuid.uuid4)
    download_url = models.CharField(null= True, default= None, blank = True, max_length=255)
    storage_id = models.CharField(null= True, default= None, blank = True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_created)


class AppUser(models.Model):
    id = models.CharField(max_length = 100, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(null=True, max_length=255)
    auth_id = models.CharField(null=True, blank = True,max_length=255)
    phone_number = models.CharField(null=True, blank = True,max_length=50)
    email = models.EmailField(null=True)
    photo_url = models.CharField(null=True, blank = True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    

class BinCategory(models.Model):
    id = models.CharField(verbose_name="id", primary_key=True, max_length=55, unique=True)
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Bin Categories"


class TrashBin(models.Model):
    id = models.CharField(verbose_name="id", primary_key=True, max_length=55, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True, default=None)
    location_x = models.IntegerField(blank=True)
    location_y = models.IntegerField(blank=True)  # Note: there's still a typo here "locaiton_y"
    categories = models.ManyToManyField(BinCategory, blank=True)
    added_by = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ManyToManyField(ImageModel, blank=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        categories_list = self.categories.all()
        if categories_list:
            return ", ".join(str(category) for category in categories_list)
        return "Uncategorized"



