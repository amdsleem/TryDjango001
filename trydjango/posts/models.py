from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# from django.core.urlresolvers import reverse

# Create your models here.
#MVC MODEL VIEW CONTROLLER

#upload function to define where is file will be uploaded
#its generate a new folder with our file name
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" %(instance.id, filename)



class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
        )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/posts/%s/" % self.id
        return reverse("posts:detail", kwargs={"id": self.id})
    
    class Meta:
        ordering = ["-timestamp", "-update"]
