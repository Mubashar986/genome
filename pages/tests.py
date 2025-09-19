from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class TestHomepage(SimpleTestCase):
    def test_url_exist_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
    def test_url_avaiable_byname(self):
            response=self.client.get(reverse("home"))
        
            self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"pages/home.html")
    
    def test_template_content_available(self):
        response=self.client.get(reverse("home"))
        self.assertContains(response,"<h1>class based views</h1>")
    




class Testpagetest(SimpleTestCase):
    def test_url_exist_location(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code,200)

    def test_url_avaiable_byname(self):
        response=self.client.get(reverse("about"))
        
        self.assertEqual(response.status_code,200)


    def test_template_name_correct(self):
        response=self.client.get(reverse("about"))
        self.assertTemplateUsed(response,"pages/about.html")
    
    def test_template_content_available(self):
        response=self.client.get(reverse("about"))
        self.assertContains(response,"<h1>hey we have been working</h1>")
    
    