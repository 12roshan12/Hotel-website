from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email does not exists')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super user must be true')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=False)
    last_name = models.CharField(_('last name'), max_length=50, blank=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_employee = models.BooleanField(_('is employee'), default=False)
    is_customer = models.BooleanField(_('is customer'), default=False)

    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'user'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profiles', on_delete=models.CASCADE)
    birth_day = models.DateField(default=None, blank=True, null=True)
    mobile_number = models.CharField(blank=True, null=True, max_length=100)
    avatar = models.ImageField(default='users/avatar.png', blank=True, null=True, upload_to='users')
    location = models.CharField(blank=True, null=True, max_length=100)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        db_table = 'user_profiles'
        verbose_name_plural = 'Profile'
        ordering = ('-id',)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        avatar = Image.open(self.avatar)
        if avatar.height > 200 or avatar.width > 200:
            new_size = (200, 200)
            avatar.thumbnail(new_size)
            avatar.save(self.avatar.path)


@receiver(models.signals.post_save, sender=User)
def post_save_user_signal(sender, instance, created, **kwargs):
    if created:
        instance.save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Enquiry(models.Model):
    name = models.CharField(max_length=10,default=None)
    email = models.CharField(max_length=10)
    number = models.CharField(max_length=15,default=None)
    message = models.TextField(blank=True)
    

    class Meta:
        db_table = 'contact_us'
        verbose_name_plural = 'Enquiry'
       
    def __str__(self):
        return self.name   

class AboutUs(models.Model):
    title = models.CharField(max_length=100,default=None)
    description = models.TextField()
    image = models.ImageField(upload_to='images/about_us/')   
    added_by = models.CharField(max_length=30)
    created_at = models.DateTimeField( auto_now_add=True)

    class Meta:
        db_table = 'about_us'
        verbose_name_plural = 'About-Us'

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True,upload_to='images/blog/')
    added_by = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = 'blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=30,default=None)
    description  = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    venue = models.CharField(max_length=30,default=None)
    added_by = models.CharField(max_length=20,default= None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'events'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title    
       

    
       