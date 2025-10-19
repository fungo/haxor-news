from haxor_news.__init__ import __version__
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


setup(
    description=('View and filter Hacker News from the command line: '
                 'Posts, comments, and linked web content.'),
    author='Donne Martin',
    url='https://github.com/donnemartin/haxor-news',
    download_url='https://pypi.python.org/pypi/haxor-news',
    author_email='donne.martin@gmail.com',
    version=__version__,
    license='Apache License 2.0',
    install_requires=[
        'click>=8.1.8',
        'colorama>=0.4.6',
        'requests>=2.31.0,<3.0.0',
        'pygments>=2.17.0',
        'prompt-toolkit>=3.0.52',
    ],
    extras_require={
        'testing': [
            'mock>=1.0.1,<2.0.0',
            'tox>=1.9.2,<2.0.0'
        ],
    },
    entry_points={
        'console_scripts': [
            'haxor-news = haxor_news.main:cli',
            'hn = haxor_news.main_cli:cli'
        ]
    },
    packages=find_packages(),
    scripts=[],
    name='haxor-news',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
