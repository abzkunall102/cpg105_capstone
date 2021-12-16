from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + " message:  " + self.message

class MlModel(models.Model):
    image = models.FileField(upload_to='images/%Y/%m/%d')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " PATH:" + self.image.name
