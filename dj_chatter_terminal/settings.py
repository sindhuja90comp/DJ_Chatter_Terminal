import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'dev-not-secret'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'bot',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
ROOT_URLCONF = 'dj_chatter_terminal.urls'
MIDDLEWARE = []
TEMPLATES = []
WSGI_APPLICATION = 'dj_chatter_terminal.wsgi.application'
