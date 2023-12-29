from django.db import models

class Servise (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='servise/image', blank=True)
    photo_1 = models.ImageField(upload_to='servise/image', blank=True)
    slide = models.ImageField(upload_to='servise/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='servise/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Servise'
        verbose_name_plural = 'Servises'




class Frequently (models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='frequently/image', blank=True)
    photo_2 = models.ImageField(upload_to='frequently/image', blank=True)
    slide = models.ImageField(upload_to='frequently/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='frequently/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Frequently'
        verbose_name_plural = 'Frequentlys'



class Privacy_Policy(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='privacy_policy/image', blank=True)
    slide = models.ImageField(upload_to='privacy_policy/slide', blank=True)

    low_title = models.CharField(max_length=255, blank=True)
    low_about = models.CharField(max_length=255, blank=True)

    blog_title = models.CharField(max_length=255, blank=True)
    blog_photo = models.ImageField(upload_to='privacy_policy/blogs_images', blank=True)
    name = models.CharField(max_length=255, blank=True)
    time = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Privacy_Policy'
        verbose_name_plural = 'Privacy_Policys'



class Page_404(models.Model):
    title  = models.CharField(max_length=255, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='page_404/image', blank=True)
    
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = 'Page_404'
        verbose_name_plural = 'Page_404'
 
    