from .production import *

SECRET_KEY = "{{ DISCOVERY_SECRET_KEY }}"
ALLOWED_HOSTS = ["localhost", "discovery.localhost", "{{ DISCOVERY_HOST }}"]
PLATFORM_NAME = "{{ PLATFORM_NAME }}"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "{{ DISCOVERY_MYSQL_DATABASE }}",
        "USER": "{{ DISCOVERY_MYSQL_USERNAME }}",
        "PASSWORD": "{{ DISCOVERY_MYSQL_PASSWORD }}",
        "HOST": "{{ MYSQL_HOST }}",
        "PORT": "{{ MYSQL_PORT }}",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

HAYSTACK_CONNECTIONS["default"].update(
    {
        "URL": "http://{{ ELASTICSEARCH_HOST }}:{{ ELASTICSEARCH_PORT }}",
        "INDEX_NAME": "{{ DISCOVERY_INDEX_NAME }}",
    }
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_PREFIX": "discovery",
        "LOCATION": "{{ MEMCACHED_HOST }}:{{ MEMCACHED_PORT }}",
    }
}

LANGUAGE_CODE = "{{ LANGUAGE_CODE }}"
PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
PARLER_LANGUAGES[1][0]["code"] = LANGUAGE_CODE
PARLER_LANGUAGES["default"]["fallbacks"] = [PARLER_DEFAULT_LANGUAGE_CODE]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "{{ SMTP_HOST }}"
EMAIL_PORT = "{{ SMTP_PORT }}"
EMAIL_HOST_USER = "{{ SMTP_USERNAME }}"
EMAIL_HOST_PASSWORD = "{{ SMTP_PASSWORD }}"
EMAIL_USE_TLS = {{ SMTP_USE_TLS }}

LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": "/var/log/discovery.log",
    "formatter": "standard",
}

JWT_AUTH["JWT_ISSUER"] = "{{ JWT_COMMON_ISSUER }}"
JWT_AUTH["JWT_AUDIENCE"] = "{{ JWT_COMMON_AUDIENCE }}"
JWT_AUTH["JWT_SECRET_KEY"] = "{{ JWT_COMMON_SECRET_KEY }}"
SOCIAL_AUTH_EDX_OIDC_SECRET = "{{ DISCOVERY_OAUTH2_SECRET }}"
SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY = SOCIAL_AUTH_EDX_OIDC_SECRET
SOCIAL_AUTH_EDX_OIDC_ISSUER = "http://localhost:8000/oauth2"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = {% if ACTIVATE_HTTPS %}True{% else %}False{% endif %}
SOCIAL_AUTH_EDX_OIDC_KEY = "{{ DISCOVERY_OAUTH2_KEY }}"
# The following urls should be accessible from the outside by a discovery web user in
# order to use the /login endpoint
SOCIAL_AUTH_EDX_OIDC_URL_ROOT = "{% if ACTIVATE_HTTPS %}https{% else %}http{% endif %}://{{ LMS_HOST }}/oauth2"
SOCIAL_AUTH_EDX_OIDC_LOGOUT_URL = "{% if ACTIVATE_HTTPS %}https{% else %}http{% endif %}://{{ LMS_HOST }}/logout"
SOCIAL_AUTH_EDX_OIDC_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OIDC_URL_ROOT
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = SOCIAL_AUTH_EDX_OIDC_URL_ROOT
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = SOCIAL_AUTH_EDX_OIDC_URL_ROOT

EDX_DRF_EXTENSIONS = {
    'OAUTH2_USER_INFO_URL': '{% if ACTIVATE_HTTPS %}https{% else %}http{% endif %}://{{ LMS_HOST }}/oauth2/user_info',
}

STATIC_ROOT = "/openedx/static"
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
