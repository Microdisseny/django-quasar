from distutils.core import setup

from setuptools import find_packages

VERSION = '0.0.1'

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python :: 3',
    'Environment :: Web Environment',
    'Development Status :: 4 - Beta',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='django_quasar',
    description='Django: Add Quasar media files ',
    version=VERSION,
    author='MICRODISSENY GISCUBE SL',
    author_email='tech@microdisseny.com',
    license='MIT License',
    platforms=['OS Independent'],
    url='https://github.com/Microdisseny/django-quasar',
    packages=find_packages(exclude=['__pycache__']),
    include_package_data=True,
    classifiers=CLASSIFIERS,
    zip_safe=False,
    install_requires=[]
)
