from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.models import AbstractUser


class Banner(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to='banner_img/')

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=55, verbose_name='Nomi')
    description = models.CharField(max_length=555, verbose_name='Malumot')
    img = models.ImageField(upload_to='about_img/')

    def __str__(self):
        return self.title


class Pricing(models.Model):
    room_type = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    capacity = models.IntegerField(default=1, verbose_name='Odam_sigmi')
    services = models.CharField(max_length=255, verbose_name='Xonani qulayliklari')
    img = models.ImageField(upload_to='pricing_img/')

    def __str__(self):
        return self.room_type





class Room(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/')
    description = models.TextField()
    capacity = models.IntegerField()
    contact_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])
    contact_email = models.EmailField(validators=[EmailValidator(message="Email manzilingiz noto'g'ri")])

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Band qilish'
        verbose_name_plural = 'Band qilishlar'

    def __str__(self):
        return f"{self.user} - {self.room} - {self.start_date}"


class Service(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'

    def __str__(self):
        return self.name




class Our_services(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Info(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])
    extra_phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamingiz noto'g'ri")])
    instagramm = models.CharField(max_length=55)



    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    img = models.ImageField(upload_to='gallery/')
    ROOM_TYPE_CHOICES =[
        ('Econom', 'Econom'),
        ('Comfort', 'Comfort'),
        ('Lux', 'Lux')
    ]
    title = models.CharField(max_length=25, choices=ROOM_TYPE_CHOICES)


