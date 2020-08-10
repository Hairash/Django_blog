from django.db import models
from tinymce import models as tinymce_models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = tinymce_models.HTMLField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return str(self.title)


