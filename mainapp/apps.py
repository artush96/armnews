from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainapp'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
