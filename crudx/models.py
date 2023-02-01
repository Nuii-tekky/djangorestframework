from django.db import models

# Create your models here.

class StudentsData(models.Model):

  firstname     = models.CharField(max_length= 70)
  lastname      = models.CharField(max_length= 70)
  age           = models.IntegerField()
  height        = models.DecimalField(decimal_places=2,max_digits=67)
  Darkskinned   = models.BooleanField()
  created_at    = models.DateTimeField(auto_now_add= True)

  def __str__(self):
    return self.firstname.title() + ' '+ self.lastname.title()

