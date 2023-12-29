from django.db import models

class About_us (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='about_us/image', blank=True)
    photo_1 = models.ImageField(upload_to='about_us/image', blank=True)
    slide = models.ImageField(upload_to='about_us/slide', blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='about_us/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'About_us'
        verbose_name_plural = 'About_us'

