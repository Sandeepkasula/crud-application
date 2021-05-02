from django.db import models

# Create your models here.
from django.db import models
#DataFlair Models
class moodle(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    describe = models.TextField(default = 'decribe about the course')
    def __str__(self):
        return self.name