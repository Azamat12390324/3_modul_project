from django.db import models

class Grid_Left (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='grid_left/image', blank=True)
    slide = models.ImageField(upload_to='grid_left/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='grid_left/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Grid_left'
        verbose_name_plural = 'Grid_lefts'




class Full_width (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='full_width/image', blank=True)
    slide = models.ImageField(upload_to='full_width/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='full_width/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Full_width'
        verbose_name_plural = 'Full_widths'



class List_sidebar(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='list-sidebar/image', blank=True)
    slide = models.ImageField(upload_to='list-sidebar/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='list-sidebar/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'List-sidebar'
        verbose_name_plural = 'List-sidebars'

       