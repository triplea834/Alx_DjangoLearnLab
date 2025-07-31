from django.db import models

class CustomUser(AbstractUser):, date_of_birth, profile_photo
class CustomUserManager(BaseUserManager):, create_user, create_superuser
can_create, can_delete 
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title



