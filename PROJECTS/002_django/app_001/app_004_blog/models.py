from django.db import models
from datetime import datetime
# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=100,verbose_name="Author")
    title = models.CharField(max_length=100,verbose_name="Title")
    content = models.TextField(max_length=100000,verbose_name="Content")
    created_date=models.DateTimeField(default=datetime.now,blank=True,verbose_name="Created date")
    files = models.FileField(blank=True , null=True , verbose_name="File",upload_to="media/")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
