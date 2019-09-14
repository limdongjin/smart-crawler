import io
from setuptools import setup, find_packages


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='smart-crawler',
    version='0.2',
    url='https://github.com/limdongjin/smart-crawler',
    license='MIT',
    author='limdongjin',
    author_email='geniuslim27@gmail.com',
    description='Smart Crawler',
    packages=find_packages(),
    long_description=long_description(),
    zip_safe=False,
    install_requires=['Click',
                      'beautifulsoup4',
                      'requests',
                      'selenium',
                      'lxml',
                      'pyfunctional',
                      'boto3',
                      'awscli'],
    entry_points={
        'console_scripts': ['smart-crawler = cli.main:main']
    }
)
