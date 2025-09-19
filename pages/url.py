from django.urls import path,include
from .views import home_view_request ,about_page


urlpatterns=[
    
    path("about/",about_page.as_view(),name="about"),
    path("",home_view_request,name="home")
    
]