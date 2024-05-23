from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    adharcard = models.CharField(max_length=12, unique=True)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'CustomUser'
    def __str__(self):
        return self.email
