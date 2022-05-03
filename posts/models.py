from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    commentary = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.commentary

    class Meta:
        ordering = ['created']

    class Meta:
        db_table = "blog_member"


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='DataFlair Django tutorials')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мақала"
        verbose_name_plural = "Мақалалар"
        ordering = ['-author', '-title']


class Categories(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    picture = models.ImageField(default='default value')
    describe = models.TextField(default='DataFlair Django tutorials')


class Posts2(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тақырып")
    is_published = models.BooleanField(default=True, verbose_name="Шығарылым")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class RegUser(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="First name")
    lastname = models.CharField(max_length=255, verbose_name="Last name")
    user_id = models.PositiveIntegerField(primary_key=True, default=1)
    GChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GChoices)
    email = models.EmailField(validators=[MinLengthValidator(10)])
    username = models.CharField(max_length=255, verbose_name="Username")
    password = models.CharField(max_length=255)


