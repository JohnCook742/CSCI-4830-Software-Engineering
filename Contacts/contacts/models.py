from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=320)

    def __str__(self):
        return self.name