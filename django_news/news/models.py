from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
