import django

DEBUG = True
USE_TZ = True

SECRET_KEY = "nonsensevalue"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        # "NAME": ":memory:",
        "NAME": "db",
    }
}

ADMIN_URL = "admin/"

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django_calendardate",
]

SITE_ID = 1


MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["stream"],
            "level": "ERROR",
            "propagate": True,
        },
        "django_calendardate": {
            "handlers": ["stream"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

FISCAL_YEAR_START_MONTH = 10
