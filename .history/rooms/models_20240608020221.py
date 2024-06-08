from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class room(models.Model):
    hotels=class (models.Model):
    
        
    
        class Meta:
            verbose_name = _("")
            verbose_name_plural = _("s")
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("_detail", kwargs={"pk": self.pk})
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    roomName=models.CharField(max_length=100)
    roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomimages")