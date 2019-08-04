import io
from setuptools import setup, find_packages


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(
    name='smart-crawller',
    version='0.1',
    url='https://github.com/limdongjin/smart-crawller',
    license='MIT',
    author='limdongjin',
    author_email='geniuslim27@gmail.com',
    description='Smart Crawller',
    packages=find_packages(),
    long_description=long_description(),
    zip_safe=False,
    install_requires=['Click', 'beautifulsoup4', 'requests', 'selenium'],
    entry_points={
        'console_scripts': ['smart-crawller = cli.main:main']
    }
)
