from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    user = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name
