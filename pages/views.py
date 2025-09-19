from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView 

def home_view_request(request):
    context = {
        "inventory_list": ["vanity", "toxicty"],
        "greetings": "vanity is my favourite sin",
    }
    return render(request, "pages/home.html", context)

class about_page(TemplateView):
    template_name="pages/about.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["number"]="3432"
        context["name"]="mubashar"
        return context       

