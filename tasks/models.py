from django.db import models

# Create your models here.
class ItemModel(models.Model):
    # What are the fields inside this model (i.e, the attributes)
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False)
    
    def __str__(self):
        return self.name