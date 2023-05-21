from django.db import models
from django.contrib.auth import get_user_model

# User
User = get_user_model()


# Profile
class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_obj', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_images')
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    class Meta:
        db_table = "profile"
