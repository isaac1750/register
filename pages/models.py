from django.db import models
# from django.conf import settings
# from django.contrib.redirects.models import Redirect

# # Create your models here.
# redirect = Redirect.objects.create(

#     site_id=1,
#     old_path='/admin/',pyth
#     new_path='/me/',
#  )

# Create your models here.
class Submit(models.Model):
    email = models.EmailField(max_length=20)
    name= models.CharField(max_length=15)
    address1 = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    class Meta:
    	permissions = (


    	    ("about", "about"), 
    	)
    


    def __str__(self):
        return self.email