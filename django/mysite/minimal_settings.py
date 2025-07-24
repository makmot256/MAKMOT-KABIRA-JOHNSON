from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'temporary'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
INSTALLED_APPS = []  # Empty list ensures no dependencies
MIDDLEWARE = []
ROOT_URLCONF = None
STATIC_URL = '/static/'  # Only needed if using staticfiles