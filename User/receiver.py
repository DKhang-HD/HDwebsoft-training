from django.dispatch import receiver
from .signal import signup_done
from .views import SignUpView


@receiver(signup_done, sender=SignUpView)
def confirm_signup(sender, **kwargs):
    print('You signup successfully')
    print('sender', sender)
