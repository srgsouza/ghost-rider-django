from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    img_url = models.CharField(max_length=500)
    # images = models.ImageField(upload_to='car_image', blank=True)
    description = models.CharField(max_length=800)
    owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    def save(self, *args, **kwargs):
        super(Car, self).save(*args, **kwargs)    
    
class Comment(models.Model):
    comment = models.CharField(max_length=280)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


