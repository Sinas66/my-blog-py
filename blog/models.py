from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300, blank=False)
    date = models.DateTimeField()
    text = models.TextField(max_length=300)
    image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.text[:70] + " ..."

    def __str__(self):
        return self.title