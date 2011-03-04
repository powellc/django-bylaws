from setuptools import setup, find_packages
 
setup(
    name='django-bylaws',
    version='0.1.0',
    description='Manage bylaws in on a Django-powered site.',
    author='Colin Powell',
    author_email='colin@onecardinal.com',
    url='http://github.com/powellc/django-bylaws/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

