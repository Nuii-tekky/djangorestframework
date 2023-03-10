from django.db import models

# Create your models here.

class StudentsData(models.Model):

  firstname     = models.CharField(max_length= 70,blank= True,null= True)
  lastname      = models.CharField(max_length= 70,blank= True,null= True)
  age           = models.IntegerField(blank= True,null= True)
  height        = models.DecimalField(decimal_places= 2,max_digits=10,blank= True,null= True)
  Darkskinned   = models.BooleanField(blank= True,null= True)
  created_at    = models.DateTimeField(auto_now_add= True)

  def __str__(self):
    return self.firstname.title() + ' '+ self.lastname.title()

class RandomWord(models.Model):
  word= models.CharField(max_length=34)

  def __str__(self) -> str:
    return self.word.title()


class images(models.Model):
  title= models.CharField(max_length= 70,blank= True,null= True)
  img= models.ImageField(upload_to= "api_img_upl",blank= True,null= True)
  def __str__(self) -> str:
    return self.title.title()

  