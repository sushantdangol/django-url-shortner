from django.db import models

# Create your models here.
class UrlModel(models.Model):
    token = models.CharField(max_length=6, primary_key=True, default=None)
    url = models.URLField()
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
        
    class Meta:
        ordering = ('-published_date',)
