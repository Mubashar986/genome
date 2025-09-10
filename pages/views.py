from django.shortcuts import render
from django.http import HttpResponse




def home_view_request(request):
    return HttpResponse("hey I am doing django")

def other_veiw(request):
    name=input("Enter ur name")
    return HttpResponse(name)



