# Generated by Django 5.0 on 2023-12-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frequently',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='frequently/image')),
                ('photo_2', models.ImageField(blank=True, upload_to='frequently/image')),
                ('slide', models.ImageField(blank=True, upload_to='frequently/slide')),
                ('low_title', models.CharField(blank=True, max_length=255)),
                ('low_about', models.CharField(blank=True, max_length=255)),
                ('blog_title', models.CharField(blank=True, max_length=255)),
                ('blog_photo', models.ImageField(blank=True, upload_to='frequently/blogs_images')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': 'Frequently',
                'verbose_name_plural': 'Frequentlys',
            },
        ),
        migrations.CreateModel(
            name='Page_404',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='page_404/image')),
            ],
            options={
                'verbose_name': 'Page_404',
                'verbose_name_plural': 'Page_404',
            },
        ),
        migrations.CreateModel(
            name='Privacy_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='privacy_policy/image')),
                ('slide', models.ImageField(blank=True, upload_to='privacy_policy/slide')),
                ('low_title', models.CharField(blank=True, max_length=255)),
                ('low_about', models.CharField(blank=True, max_length=255)),
                ('blog_title', models.CharField(blank=True, max_length=255)),
                ('blog_photo', models.ImageField(blank=True, upload_to='privacy_policy/blogs_images')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': 'Privacy_Policy',
                'verbose_name_plural': 'Privacy_Policys',
            },
        ),
        migrations.CreateModel(
            name='Servise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='servise/image')),
                ('photo_1', models.ImageField(blank=True, upload_to='servise/image')),
                ('slide', models.ImageField(blank=True, upload_to='servise/slide')),
                ('low_title', models.CharField(blank=True, max_length=255)),
                ('low_about', models.CharField(blank=True, max_length=255)),
                ('blog_title', models.CharField(blank=True, max_length=255)),
                ('blog_photo', models.ImageField(blank=True, upload_to='servise/blogs_images')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateField(blank=True)),
            ],
            options={
                'verbose_name': 'Servise',
                'verbose_name_plural': 'Servises',
            },
        ),
    ]
