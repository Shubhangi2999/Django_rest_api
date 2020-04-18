from django.db import models

class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.f_name
