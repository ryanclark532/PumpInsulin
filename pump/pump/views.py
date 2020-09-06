from django.http import HttpResponse
from pump.models import User

def index(request):
    return HttpResponse("Hello Bailey")


def addUser(request,firstName,lastName,email,age,gender,bloodType):

    new=User()
    new._firstName=firstName.lower()
    new._lastName=lastName.lower()
    new._email=email.lower()
    new._age=age.lower()
    new._gender=gender.lower()
    new._bloodType=bloodType.lower()
    new.save()
    return HttpResponse("<h1>{}</h1>".format(firstName))


def getUser(request,firstName,lastName):
    all_user_data=User.objects.get(_firstName=firstName,_lastName=lastName)
    return HttpResponse(all_user_data)



def setUser(request,firstName,lastName,email,age,gender,bloodType):
    obj=User.objects.get(_firstName=firstName,_lastName=lastName)
    obj._firstName=firstName
    obj._lastName=lastName
    obj._email=email
    obj._age=age 
    obj._gender=gender
    obj._bloodType=bloodType
    obj.save()
    return HttpResponse("<h1>{} {}</h1>".format(firstName,lastName))





