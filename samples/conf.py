from django.conf import settings
from appconf import AppConf

class MyAppConf(AppConf):
    MULTIPLY_A = 100

    class Meta:
        prefix = 'samples'