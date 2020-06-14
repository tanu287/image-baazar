from django.db import models

# Create your models here.
#Create categories model.

class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

#create Image models
class Image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='images', default="")
    pub_date = models.DateField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
