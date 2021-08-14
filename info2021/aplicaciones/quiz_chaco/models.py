from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Pregunta(models.Model):
    title = models.TextField(null= True, blank= True)
    status = models.CharField(default='inactive', max_length=50)
    created_by = models.ForeignKey(User, null= True, blank= True, on_delete = models.CASCADE)
    pregunta=models.CharField(max_length=600, null=True)
    opcion1=models.CharField(max_length=200, null=True)
    opcion2=models.CharField(max_length=200,null=True)
    opcion3=models.CharField(max_length=200, null=True)
    opcion4=models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modify = models.BooleanField()
    
    def __str__(self):
        return self.title