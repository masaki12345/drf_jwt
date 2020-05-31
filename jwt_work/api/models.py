from django.db import models

# Create your models here.
class MainContent(models.Model):
    title = models.CharField(("メインコンテンツ"), max_length=50)
    article = models.CharField(("記事"), max_length=50)

    def __str__(self):
        return str(self.id) + self.title

class Tag(models.Model):
    tags = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    subtitle = models.CharField(("サブタイトル"), max_length=50)

    def __str__(self):
        return str(self.subtitle)