from django.apps import AppConfig
from .signal import signup_done


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'

    def ready(self):
        from .receiver import confirm_signup
        signup_done.connect(confirm_signup, dispatch_uid="my_unique_identifier")

