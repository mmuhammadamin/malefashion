from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/', null=True)
    bio = models.CharField(max_length=221)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def user_profile_post_save(instance, sender, *args, **kwargs):
    instance.profile.save()

