# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------
from cachelib.redis import RedisCache


ROW_LIMIT = 5000
SUPERSET_WEBSERVER_PORT = 18008

# Setup default language
BABEL_DEFAULT_LOCALE = 'zh'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'superset/translations'
# The allowed translation for you app
LANGUAGES = {
    'zh': {'flag': 'cn', 'name': 'Chinese'},
}

# ---------------------------------------------------
# Roles config
# ---------------------------------------------------
# Grant public role the same set of permissions as for the GAMMA role.
# This is useful if one wants to enable anonymous users to view
# dashboards. Explicit grant on specific datasets is still required.
PUBLIC_ROLE_LIKE_GAMMA = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# Uncomment to setup Your App name
APP_NAME = 'James-Superset'

# Uncomment to setup an App icon
# APP_ICON = '/static/assets/images/superset-logo@2x.png'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://developer:developer1qazXSW@@localhost/superset?charset=utf8'

CACHE_TYPE = "RedisCache"

# add on 2022-10-26
#from cachelib.redis import RedisCache
RESULTS_BACKEND = RedisCache(host='localhost', port=6379, key_prefix='superset_results')


# ADD on 2022-10-16
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_CELERY_DB = 2
REDIS_RESULTS_DB = 3
REDIS_CACHE_DB = 4

class CeleryConfig(object):
    BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    CELERY_IMPORTS = ("superset.sql_lab",)
    CELERY_ANNOTATIONS = {"sql_lab.add": {"rate_limit": "10/s"}}
    CONCURRENCY = 1

CELERY_CONFIG = CeleryConfig

# Default cache for Superset objects
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 3600,
    "CACHE_KEY_PREFIX": "superset_cache",
    "CACHE_REDIS_URL": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}",
}

# Cache for datasource metadata and query results
DATA_CACHE_CONFIG = {
    **CACHE_CONFIG,
    "CACHE_DEFAULT_TIMEOUT": 3600,
    "CACHE_KEY_PREFIX": "superset_data_cache",
}

COMPRESS_REGISTER = True
