from django.apps import AppConfig


class SoloAppConfig(AppConfig):
    name = 'sw_solo'
    verbose_name = "solo"
    verbose_name_plural = "solo"

default_app_config = 'sw_solo.SoloAppConfig'

