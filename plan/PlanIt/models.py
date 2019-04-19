from datetime import timezone
from datetime import date
from django.db import models
import datetime
from PIL import Image
class Post(models.Model):
    post_created_at = models.DateTimeField( auto_now_add=True)#auto_created=True)
  #  post_updated_at = models.DateTimeField(auto_now_add=True,auto_created=True)

    post_text = models.TextField(max_length=100000)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.post_text
    # seller forieng key

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='images')


   # time
    #seller foreign key


#class Favourite(models.Model):
