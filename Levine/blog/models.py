
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=200)
  text=models.TextField()
 # author = models.ForeignKey(get_user_model(),null=True)
  date_created=models.DateTimeField(auto_now_add=True)
  date_published=models.DateTimeField(default=timezone.now)