from setuptools import setup

setup(
    name='template3',
    version='0.2',
    author='Kelvin Jayanoris',
    author_email='kelvin@jayanoris.com',
    install_requires=[
        'django',
        'django-allauth',
        'django-braces',
        'django-compressor',
        'django-crispy-forms',
        'django-debug-toolbar',
        'django-extensions',
        'django-tables2',
        'whitenoise'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
    ],
)
