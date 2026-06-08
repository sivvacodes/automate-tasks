from django.db import models

# Create your models here.

class Student_data(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    latitude=models.FloatField()
    longitude=models.FloatField()
    gender=models.CharField(max_length=5)
    ethnic_group=models.CharField(max_length=20)
    age=models.IntegerField()
    english_grade=models.CharField()
    math_grade=models.CharField()
    sciences_grade=models.CharField()
    language_grade=models.CharField()
    portfolio_rating=models.CharField()
    coverletter_rating=models.CharField()
    refletter_rating=models.CharField()




    def __str__(self):
        return self.name



#id,name,nationality,city,latitude,longitude,gender,ethnic.group,age,english.grade,math.grade,sciences.grade,language.grade,portfolio.rating,coverletter.rating,refletter.rating