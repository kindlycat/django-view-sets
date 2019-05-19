import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
SECRET_KEY = '43s%srs!f4m7#vdk^el3_rf2ae3szu2-ncr3+k4vu%(k=nz#q-'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tests.test_app',
    'tests.test_app.test_models',
    'tests.test_app.news',

    'viewsets',
    'django_jinja',
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'viewsets/locale'),
)

LOGIN_REDIRECT_URL = '/staff/'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

DATETIME_FORMAT = 'd E Y, H:i'

LANGUAGE_CODE = 'en'

USE_TZ = True
USE_L10N = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tests.test_app.urls'

TEMPLATES = [
    # {
    #     'BACKEND': 'django_jinja.backend.Jinja2',
    #     'DIRS': [
    #         os.path.join(BASE_DIR, 'tests/test_app/jinja2'),
    #         os.path.join(BASE_DIR, 'tests/test_app/templates')
    #     ],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'app_dirname': 'jinja2',
    #         'match_extension': '.html',
    #         'context_processors': [
    #             'django.contrib.auth.context_processors.auth',
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.i18n',
    #             'django.template.context_processors.media',
    #             'django.template.context_processors.static',
    #             'django.template.context_processors.tz',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     }
    # },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

FORM_RENDERER = 'django.forms.renderers.Jinja2'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
