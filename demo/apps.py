from django.apps import AppConfig

#настройки метаданные нашего приложения: id, name ....
class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'
