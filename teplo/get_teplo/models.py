from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField





class Articles(models.Model):
    title = models.CharField(max_length=100)
    article = RichTextUploadingField()
    created_at = models.DateField(default=timezone.now)
    image = models.ImageField(default='default.jpg')
    url = models.SlugField(default="coc")

    def __str__(self):
        return self.title
    


