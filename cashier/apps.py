from django.apps import AppConfig


class CashierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cashier'


    def ready(self):
        from cashier import signals
