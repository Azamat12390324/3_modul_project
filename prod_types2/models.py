from django.db import models

class Tab_left (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='tab_left/image', blank=True)
    photo_1 = models.ImageField(upload_to='tab_left/image', blank=True)
    slide = models.ImageField(upload_to='tab_left/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='tab_left/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Tab_left'
        verbose_name_plural = 'Tab_lefts'




class Gallery_left (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='gallery_left/image', blank=True)
    slide = models.ImageField(upload_to='gallery_left/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='gallery_left/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Gallery_left'
        verbose_name_plural = 'Gallery_lefts'



class Sticky_left(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='sticky_left/image', blank=True)
    slide = models.ImageField(upload_to='sticky_left/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='sticky_left/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Sticky_left'
        verbose_name_plural = 'Sticky_lefts'

