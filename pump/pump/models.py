from django.db import models

class User(models.Model):

    _firstName=models.CharField(max_length=50)
    _lastName=models.CharField(max_length=50)
    _email=models.CharField(max_length=50)
    _age=models.CharField(max_length=50)
    _gender=models.CharField(max_length=50)
    _bloodType=models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {} {} {} {} ".format(self._firstName,self._lastName,self._email,self._age
                               ,self._gender,self._bloodType)
class Doctor(models.Model):
    name=models.CharField(max_length=50)
 
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    bloodType=models.CharField(max_length=50)
    ahpra=models.CharField(max_length=50)

class Doseage(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    time=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)


class Pump(models.Model):
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    storedInsulin=models.FloatField()
    warningPercent=models.IntegerField()
