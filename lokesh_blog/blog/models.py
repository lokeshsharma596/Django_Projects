from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Post(models.Model):
   title=models.CharField(max_length=100)
   content=models.TextField()
   date_posted=models.DateTimeField(default=timezone.now)
   author=models.ForeignKey(User,on_delete=models.CASCADE)

class profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image= models.ImageField(default='default.jpg', upload_to='profile_pics')

   def __str__(self):
      return f'{self.user.username} Profile'

   def save(self):
      super().save()

      img = Image.open(self.image.path)

      if img.height >300 or img.width > 300:
         output_size = (300,300)
         img.thumbnail(output_size)
         img.save(self.image.path)