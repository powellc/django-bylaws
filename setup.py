from setuptools import setup, find_packages

setup(
    name='django-bylaws',
    version=__import__('bylaws').__version__,
    license="BSD",

    install_requires = [
        'django-markup-mixin',
        'django-extensions',
        'simple_history',],

    description='Manages bylaws for a website built on Django.',
    long_description=open('README.md').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-bylaws',
    download_url='http://github.com/powellc/django-bylaws/downloads',

    include_package_data=True,

    packages=['bylaws'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
