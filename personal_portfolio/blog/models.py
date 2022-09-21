from django.db import models

# Create your models here.
class project_blog(models.Model):
      title = models.CharField(max_length=100)
      description = models.TextField(max_length=2000, default='DEFAULT VALUE')
      date = models.DateField(default='2020-10-10')

      def __str__ (self):
          return(self.title)