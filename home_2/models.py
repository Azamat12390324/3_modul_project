from django.db import models

class Home_2(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='home_2/image', blank=True)
    slide = models.ImageField(upload_to='home_2/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='home_2/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)
    
    icons = models.ImageField(upload_to='home_2/icons/', blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Home_2'
        verbose_name_plural = 'Homes_2'

       

