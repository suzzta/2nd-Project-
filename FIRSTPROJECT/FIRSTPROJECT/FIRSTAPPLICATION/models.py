from django.db import models

# Create your models here.

class Candidates(models.Model):
    CandidateId=models.CharField(max_length=30)
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    ContactAddress=models.CharField(max_length=30)