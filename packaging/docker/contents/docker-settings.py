from os import environ

ALLOWED_HOSTS = ["*"]
# Si se descomenta esta línea, el panel de administración deja de funcionar correctamente
#DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]
BASEURL = 'http://0.0.0.0:80'
APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}

USE_SQLITE = bool(environ.get('DB_USE_SQLITE'))

if USE_SQLITE:
    DB_ENGINE = 'django.db.backends.sqlite3'
else:
    DB_ENGINE = 'django.db.backends.postgresql'

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': environ.get('DB_NAME', ('data/decide.sqlite3' if USE_SQLITE else 'decide')),
        'USER': environ.get('DB_USER', (None if USE_SQLITE else 'decide')),
        'PASSWORD': environ.get('DB_PASSWORD', (None if USE_SQLITE else 'decide')),
        'HOST': environ.get('DB_HOST', (None if USE_SQLITE else 'postgresql')),
        'PORT': environ.get('DB_PORT', (None if USE_SQLITE else '5432')),
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
