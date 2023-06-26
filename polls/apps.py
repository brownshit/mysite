from django.apps import AppConfig
#polls는 앱이다.

class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
