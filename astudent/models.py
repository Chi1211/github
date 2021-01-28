from django.db import models

# Create your models here.
class StudentModel(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	birthday=models.DateField()
	address=models.TextField()