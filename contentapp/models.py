from django.db import models

# Create your models here.

class Content(models.Model):
    image = models.ImageField(upload_to='content/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
