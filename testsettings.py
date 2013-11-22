import os.path

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

def abs_path(relative_path, base_dir=PROJECT_DIR):
    """
    Make relative paths absolute to the project directory.
    """
    return os.path.abspath(os.path.join(base_dir, relative_path))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'stub-value-for-django'

INSTALLED_APPS = (
    'django.contrib.sessions',
    'url_history',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'url_history.middleware.URLHistoryMiddleware',
)

ROOT_URLCONF = 'url_history.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    abs_path('test_templates'),
)
