from django.db import models

from PIL import Image

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True, max_length=50)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    re_password = models.CharField(max_length=100)
    role = models.CharField(max_length=40)
    college = models.CharField(max_length=60)
    HSC = models.CharField(max_length=100)
    marks1 = models.CharField(max_length=100)
    SSC = models.CharField(max_length=100)
    marks2 = models.CharField(max_length=100)
    graduation = models.CharField(max_length=100) 
    marks3 = models.CharField(max_length=100)
    post_graduation = models.CharField(max_length=100)
    marks4 = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    company1 = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company2 = models.CharField(max_length=100)
    box1 = models.CharField(max_length=100)
    box2 = models.CharField(max_length=100)
    Salary1 = models.CharField(max_length=100)
    Salary2 = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    Accomplishment= models.CharField(max_length=100)
    Hobby = models.CharField(max_length=100)
    References = models.CharField(max_length=100)
    DOB = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Languages =models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True)
    
    class Meta:
        db_table = "Users"

class Category(models.Model):
    cid = models.CharField(max_length=50)
    ctype = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.ctype

    

class Aptitude(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Aptitude"
        
class Technical(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Technical"  

class Aptitude1(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Aptitude1"
        
class Technical1(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Technical1" 

class Aptitude2(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Aptitude2"
        
class Technical2(models.Model):
    qid = models.IntegerField()
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct = models.CharField(max_length=30)
    
    class Meta:
        db_table = "Technical2"        
               
        

class Listquestions(models.Model):

    username = models.EmailField(max_length=100)
    qid=models.CharField(max_length=50)
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct= models.CharField(max_length=500,default="A")
    qtype=models.CharField(max_length=100,default="apti")
    
    class Meta:
        db_table = "Listquestions"          

class Check_Select(models.Model):
    qid=models.CharField(max_length=50)
    Question = models.CharField(max_length=1000)
    optionA=models.CharField(max_length=500)
    optionB = models.CharField(max_length=500)
    optionC= models.CharField(max_length=500)
    optionD= models.CharField(max_length=500)
    correct= models.CharField(max_length=500,default="A")
    qtype=models.CharField(max_length=100,default="apti")
    
    class Meta:
        db_table="Check_Select"

class quizattempt(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    test = models.CharField(max_length=100,default="test")
  
    class Meta:
        db_table = "quizattempt" 

class quizattempt1(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    test = models.CharField(max_length=100,default="test1")

    class Meta:
        db_table = "quizattempt1" 

class quizattempt2(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
  
    class Meta:
        db_table = "quizattempt2"           
        
        
class Finalresults(models.Model):
    #sid=models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    year = models.CharField(max_length=100)
    college= models.CharField(max_length=100)
    branch= models.CharField(max_length=100)
    div= models.CharField(max_length=100)
    strtime= models.CharField(max_length=100)
    endtime= models.CharField(max_length=100)
    marks= models.CharField(max_length=100)
    
    class Meta:
        db_table = "Finalresults"     

     