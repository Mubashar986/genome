from django.urls import path,include
from .views import home_view_request,other_veiw


urlpatterns=[
    
    path("",home_view_request),
    path("other/",other_veiw)
    
]