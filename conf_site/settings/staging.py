from .base import *  # noqa: F403
from .secrets import *  # noqa: F403


DEBUG = False

DATABASES = {
    "default": DATABASES_DEFAULT,       # noqa: F405
}

SECURE_SSL_REDIRECT = True
