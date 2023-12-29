from django.db import models


class Contact_us (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='contact_us/image', blank=True)
    photo_1 = models.ImageField(upload_to='contact_us/image', blank=True)
    slide = models.ImageField(upload_to='contact_us/slide', blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='contact_us/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Contact_us'
        


