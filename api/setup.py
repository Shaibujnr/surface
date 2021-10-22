from setuptools import setup, find_packages

setup(
    name='surface',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "affine==2.3.0",
        "amqp==5.0.6",
        "appdirs==1.4.4",
        "attrs==21.2.0",
        "Cartopy==0.18.0",
        "celery==5.1.2",
        "cronex==0.1.3.1",
        "Django==3.2.8",
        "django-celery-beat==2.2.1",
        "django-colorfield==0.4.4",
        "django-cors-headers==3.10.0",
        "django-import-export==2.6.1",
        "django-material==1.9.0",
        "djangorestframework==3.12.4",
        "djangorestframework-simplejwt==4.8.0",
        "geopandas==0.10.1",
        "matplotlib==3.4.3",
        "MetPy==1.1.0",
        "opencv-python==4.5.3.56",
        "pandas==1.3.3",
        "psycopg2-binary==2.9.1",
        "PyJWT==2.2.0",
        "pyproj==3.2.1",
        "python-memcached==1.59",
        "python-slugify==5.0.2",
        "pytz",
        "rasterio==1.2.9",
        "redis==3.5.3",
        "requests==2.26.0"
    ]
)