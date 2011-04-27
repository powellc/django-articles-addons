from setuptools import setup, find_packages

setup(
    name='django-articles-addons',
    version=__import__('articles_addons').__version__,
    license="GPLv3",

    install_requires = ['django-articles',],

    description='A collection of tools to extend codekoala\'s wonderful django-articless',
    long_description=open('README.rst').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-articles-addons',
    download_url='http://github.com/powellc/django-articles-addons/downloads',

    include_package_data=True,

    packages=['articles_addons'],

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
