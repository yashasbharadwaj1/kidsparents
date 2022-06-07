from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class places(models.Model):
    loc_to_be_searched=models.CharField(max_length=50)
    
    def __str__(self):
        return self.loc_to_be_searched


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    place = models.ForeignKey(
        places, on_delete=models.PROTECT, default=1)    
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField(blank=False)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')
    newmanager = NewManager()  # custom manager
    objects = models.Manager()  # default manager
    def get_absolute_url(self):
        return reverse('contents:post_single', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class bloodbank(Post):
    pincode=models.IntegerField()
    def __str__(self):
        return self.excerpt

class blooddonors(models.Model):
    name = models.CharField(max_length=30)
    blood_group=models.CharField(max_length=10)
    contact= models.CharField(max_length=40)
    home_address=models.CharField(max_length=100)
    
    def __str__(self):
       return self.blood_group
