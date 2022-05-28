from django.db import models

# Original Code
"""
class Signup_Form(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = "signup_table"
"""

# new code
class Signup_Form(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.CharField(max_length=3)

    #email = models.EmailField(max_length=100)
    #username = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

    class Meta:
        db_table = "final_signup_table"


# Create your models here.
