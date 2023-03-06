from django.dispatch import receiver
from .signal import signup_done, myname
from .views import SignUpView, MyUser


@receiver(signup_done, sender=SignUpView)
def confirm_signup(sender, **kwargs):
    print('You signup successfully')
    print('sender', sender)


@receiver(myname, sender=MyUser)
def show_name(sender, instance, **kwargs):
    print(instance.username)
