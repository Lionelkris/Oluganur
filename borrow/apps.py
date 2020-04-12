from django.apps import AppConfig


class BorrowConfig(AppConfig):
    name = 'borrow'

    def ready(self):
        import borrow.signals
