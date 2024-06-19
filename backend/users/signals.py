from django.dispatch import receiver
from django.db.models.signals import post_save
from customers.models import Address, Customer
from users.models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()

@receiver(post_save, sender=CustomUser)
def create_customer(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.create(user=instance, name=instance.email, email=instance.email, phone=instance.phone)
        customer.save()

@receiver(post_save, sender=CustomUser)
def create_customer_address(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.get(user=instance)
        user_address = Address.objects.create(customer=customer)
        user_address.save()

